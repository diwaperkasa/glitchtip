from datetime import datetime
from typing import Annotated, Any, Literal

from ninja import Field, ModelSchema, Schema
from pydantic import computed_field

from apps.event_ingest.schema import CSPReportSchema, EventException
from apps.projects.models import Project
from apps.users.models import User
from glitchtip.schema import CamelSchema
from sentry.interfaces.stacktrace import get_context

from ..shared.schema.contexts import Contexts
from ..shared.schema.event import (
    BaseIssueEvent,
    BaseRequest,
    EventBreadcrumb,
    ListKeyValue,
)
from ..shared.schema.user import EventUser
from .constants import IssueEventType
from .models import Comment, Issue, IssueEvent, UserReport


class ProjectReference(CamelSchema, ModelSchema):
    id: str

    class Config:
        model = Project
        model_fields = ["platform", "slug", "name"]
        populate_by_name = True

    @staticmethod
    def resolve_id(obj: Project):
        return str(obj.id)


# For Sentry compatibility
def to_camel_with_lower_id(string: str) -> str:
    return "".join(
        word if i == 0 else "Id" if word == "id" else word.capitalize()
        for i, word in enumerate(string.split("_"))
    )


class IssueSchema(ModelSchema):
    id: str
    count: str
    type: str = Field(validation_alias="get_type_display")
    level: str = Field(validation_alias="get_level_display")
    status: str = Field(validation_alias="get_status_display")
    project: ProjectReference = Field(validation_alias="project")
    shortId: str = Field(validation_alias="short_id_display")
    numComments: int = Field(validation_alias="num_comments")
    stats: dict[str, list[list[float]]] | None = {"24h": []}
    share_id: int | None = None
    logger: str | None = None
    permalink: str | None = "Not implemented"
    status_details: dict[str, str] | None = {}
    subscription_details: str | None = None
    user_count: int | None = 0
    matching_event_id: str | None = Field(
        default=None, serialization_alias="matchingEventId"
    )
    firstSeen: datetime = Field(validation_alias="first_seen")
    lastSeen: datetime = Field(validation_alias="last_seen")

    @staticmethod
    def resolve_culprit(obj: Issue):
        return obj.culprit or ""

    @staticmethod
    def resolve_matching_event_id(obj: Issue, context):
        if event_id := context["request"].matching_event_id:
            return event_id.hex

    class Config(Schema.Config):
        model = Issue
        model_fields = [
            "title",
            "metadata",
            "culprit",
        ]
        alias_generator = to_camel_with_lower_id
        coerce_numbers_to_str = True
        populate_by_name = True


class IssueDetailSchema(IssueSchema):
    userReportCount: int = Field(validation_alias="user_report_count")


class ExceptionEntryData(Schema):
    values: dict
    exc_omitted: None = None
    has_system_frames: bool


class ExceptionEntry(Schema):
    type: Literal["exception"]
    data: dict


class MessageEntry(Schema):
    type: Literal["message"]
    data: dict


class CSPEntry(Schema):
    type: Literal["csp"]
    data: dict


class APIEventBreadcrumb(EventBreadcrumb):
    """Slightly modified Breadcrumb for sentry api compatibility"""

    event_id: str | None = None


class BreadcrumbsEntry(Schema):
    type: Literal["breadcrumbs"]
    data: dict[Literal["values"], list[APIEventBreadcrumb]]


class Request(CamelSchema, BaseRequest):
    headers: ListKeyValue | None = None
    query_string: ListKeyValue | None = Field(default=None, serialization_alias="query")

    @computed_field
    @property
    def inferred_content_type(self) -> str | None:
        if self.headers:
            return next(
                (value for key, value in self.headers if key == "Content-Type"), None
            )
        return None

    class Config(CamelSchema.Config, BaseRequest.Config):
        pass


class RequestEntry(Schema):
    type: Literal["request"]
    data: Request


class IssueEventSchema(CamelSchema, ModelSchema, BaseIssueEvent):
    id: str = Field(validation_alias="id.hex")
    event_id: str
    project_id: int = Field(validation_alias="issue.project_id")
    group_id: str
    date_created: datetime
    date_received: datetime
    dist: str | None = None
    culprit: str | None = Field(validation_alias="transaction", default=None)
    packages: dict[str, str | None] | None = Field(
        validation_alias="data.modules", default=None
    )
    type: str = Field(validation_alias="get_type_display")
    message: str
    metadata: dict[str, str] = Field(default_factory=dict)
    tags: list[dict[str, str | None]] = []
    entries: list[
        Annotated[
            BreadcrumbsEntry | CSPEntry | ExceptionEntry | MessageEntry | RequestEntry,
            Field(..., discriminator="type"),
        ]
    ] = Field(default_factory=list)
    contexts: Contexts | None = None
    context: dict[str, Any] | None = None
    user: Any | None = None
    sdk: dict[str, Any] | None = None

    class Config:
        model = IssueEvent
        model_fields = ["id", "type", "title"]
        populate_by_name = True

    @staticmethod
    def resolve_date_created(obj: IssueEvent):
        return obj.timestamp

    @staticmethod
    def resolve_date_received(obj: IssueEvent):
        return obj.received

    @staticmethod
    def resolve_contexts(obj: IssueEvent):
        return obj.data.get("contexts")

    @staticmethod
    def resolve_context(obj: IssueEvent):
        return obj.data.get("extra")

    @staticmethod
    def resolve_user(obj: IssueEvent):
        return obj.data.get("user")

    @staticmethod
    def resolve_sdk(obj: IssueEvent):
        return obj.data.get("sdk")

    @staticmethod
    def resolve_group_id(obj: IssueEvent):
        return str(obj.issue_id)

    @staticmethod
    def resolve_tags(obj: IssueEvent):
        return [{"key": tag[0], "value": tag[1]} for tag in obj.tags.items()]

    @staticmethod
    def resolve_entries(obj: IssueEvent):
        entries = []
        data = obj.data
        if exception := data.get("exception"):
            exception = {"values": exception, "hasSystemFrames": False}
            # https://gitlab.com/glitchtip/sentry-open-source/sentry/-/blob/master/src/sentry/interfaces/stacktrace.py#L487
            # if any frame is "in_app" set this to True
            for value in exception["values"]:
                if (
                    value.get("stacktrace", None) is not None
                    and "frames" in value["stacktrace"]
                ):
                    for frame in value["stacktrace"]["frames"]:
                        if frame.get("in_app") is True:
                            exception["hasSystemFrames"] = True
                        if "in_app" in frame:
                            frame["inApp"] = frame.pop("in_app")
                        if "abs_path" in frame:
                            frame["absPath"] = frame.pop("abs_path")
                        if "colno" in frame:
                            frame["colNo"] = frame.pop("colno")
                        if "lineno" in frame:
                            frame["lineNo"] = frame.pop("lineno")
                            pre_context = frame.pop("pre_context", None)
                            post_context = frame.pop("post_context", None)
                            if "context" not in frame:
                                frame["context"] = get_context(
                                    frame["lineNo"],
                                    frame.get("context_line"),
                                    pre_context,
                                    post_context,
                                )

            entries.append({"type": "exception", "data": exception})

        if breadcrumbs := data.get("breadcrumbs"):
            entries.append({"type": "breadcrumbs", "data": {"values": breadcrumbs}})

        if logentry := data.get("logentry"):
            entries.append({"type": "message", "data": logentry})
        elif message := data.get("message"):
            entries.append({"type": "message", "data": {"formatted": message}})

        if request := data.get("request"):
            entries.append({"type": "request", "data": request})

        if csp := data.get("csp"):
            entries.append({"type": IssueEventType.CSP.label, "data": csp})
        return entries


class UserReportSchema(CamelSchema, ModelSchema):
    event_id: str = Field(validation_alias="event_id.hex")
    event: dict[str, str]
    date_created: datetime
    user: str | None = None

    class Config:
        model = UserReport
        model_fields = ["id", "name", "email", "comments"]
        populate_by_name = True

    @staticmethod
    def resolve_date_created(obj):
        return obj.created

    @staticmethod
    def resolve_event(obj):
        return {
            "eventId": obj.event_id.hex,
        }


# TODO: Sentry includes a full user object with its nested comments,
# so we should drop this schema once we create a full user schema
class CommentUserSchema(CamelSchema, ModelSchema):
    id: str

    class Config:
        model = User
        model_fields = [
            "email",
        ]
        populate_by_name = True

    @staticmethod
    def resolve_id(obj: User):
        return str(obj.id)


class CommentSchema(CamelSchema, ModelSchema):
    data: dict[str, str]
    type: str | None = "note"
    date_created: datetime
    user: CommentUserSchema | None

    class Config:
        model = Comment
        model_fields = ["id"]

    @staticmethod
    def resolve_data(obj: Comment):
        return {
            "text": obj.text,
        }

    @staticmethod
    def resolve_date_created(obj: Comment):
        return obj.created


class IssueEventDetailSchema(IssueEventSchema):
    user_report: UserReportSchema | None
    next_event_id: str | None = None
    previous_event_id: str | None = None

    @staticmethod
    def resolve_previous_event_id(obj):
        if event_id := obj.previous:
            return event_id.hex

    @staticmethod
    def resolve_next_event_id(obj):
        if event_id := obj.next:
            return event_id.hex


class IssueEventJsonSchema(ModelSchema, BaseIssueEvent):
    """
    Represents a more raw view of the event, built with open source (legacy) Sentry compatibility
    """

    event_id: str = Field(validation_alias="id.hex")
    timestamp: float = Field()
    x_datetime: datetime = Field(
        validation_alias="timestamp", serialization_alias="datetime"
    )
    breadcrumbs: Any | None = Field(validation_alias="data.breadcrumbs", default=None)
    project: int = Field(validation_alias="issue.project_id")
    level: str | None = Field(validation_alias="get_level_display")
    exception: Any | None = Field(validation_alias="data.exception", default=None)
    modules: dict[str, str] | None = Field(
        validation_alias="data.modules", default_factory=dict
    )
    contexts: dict | None = Field(validation_alias="data.contexts", default=None)
    sdk: dict | None = Field(validation_alias="data.sdk", default_factory=dict)
    type: str | None = Field(validation_alias="get_type_display")
    request: Any | None = Field(validation_alias="data.request", default=None)
    environment: str | None = Field(validation_alias="data.environment", default=None)
    extra: dict[str, Any] | None = Field(validation_alias="data.extra", default=None)
    user: EventUser | None = Field(validation_alias="data.user", default=None)

    class Config:
        model = IssueEvent
        model_fields = ["title", "transaction", "tags", "hashes"]

    @staticmethod
    def resolve_timestamp(obj):
        return obj.timestamp.timestamp()


class IssueEventDataSchema(Schema):
    """IssueEvent model data json schema"""

    metadata: dict[str, Any] | None = None
    breadcrumbs: list[EventBreadcrumb] | None = None
    exception: list[EventException] | None = None


class CSPIssueEventDataSchema(IssueEventDataSchema):
    csp: CSPReportSchema


class IssueTagTopValue(CamelSchema):
    name: str
    value: str
    count: int
    key: str


class IssueTagSchema(CamelSchema):
    top_values: list[IssueTagTopValue]
    unique_values: int
    key: str
    name: str
    total_values: int


class IssueHashSchema(CamelSchema):
    id: str
    latest_event: IssueEventSchema | None

    @staticmethod
    def resolve_id(obj):
        return obj.value.hex
