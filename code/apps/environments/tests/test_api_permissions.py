from django.urls import reverse
from model_bakery import baker

from glitchtip.test_utils.test_case import APIPermissionTestCase


class EnvironmentAPIPermissionTests(APIPermissionTestCase):
    def setUp(self):
        self.create_user_org()
        self.set_client_credentials(self.auth_token.token)
        self.environment = baker.make(
            "environments.Environment", organization=self.organization
        )
        baker.make(
            "environments.EnvironmentProject",
            environment=self.environment,
            is_hidden=False,
        )
        self.list_url = reverse(
            "api:list_environments",
            kwargs={"organization_slug": self.organization.slug},
        )

    def test_list(self):
        self.assertGetReqStatusCode(self.list_url, 403)
        self.auth_token.add_permission("org:read")
        self.assertGetReqStatusCode(self.list_url, 200)


class EnvironmentProjectAPIPermissionTests(APIPermissionTestCase):
    def setUp(self):
        self.create_user_org()
        self.set_client_credentials(self.auth_token.token)
        self.project = baker.make("projects.Project", organization=self.organization)
        self.environment_project = baker.make(
            "environments.EnvironmentProject",
            environment__organization=self.organization,
            project=self.project,
        )
        self.list_url = reverse(
            "api:list_environment_projects",
            args=[self.organization.slug, self.project.slug],
        )
        self.detail_url = reverse(
            "api:update_environment_project",
            args=[
                self.organization.slug,
                self.project.slug,
                self.environment_project.environment.name,
            ],
        )

    def test_list(self):
        self.assertGetReqStatusCode(self.list_url, 403)
        self.auth_token.add_permission("project:read")
        self.assertGetReqStatusCode(self.list_url, 200)

    def test_update(self):
        self.auth_token.add_permission("project:read")
        data = {"name": "a", "isHidden": True}
        self.assertPutReqStatusCode(self.detail_url, data, 403)

        self.auth_token.add_permission("project:write")
        self.assertPutReqStatusCode(self.detail_url, data, 200)
