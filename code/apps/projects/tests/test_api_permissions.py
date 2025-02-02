from django.urls import reverse
from model_bakery import baker

from apps.organizations_ext.models import OrganizationUserRole
from glitchtip.test_utils.test_case import APIPermissionTestCase


class ProjectAPIPermissionTests(APIPermissionTestCase):
    def setUp(self):
        self.create_user_org()
        self.set_client_credentials(self.auth_token.token)
        self.team = baker.make("teams.Team", organization=self.organization)
        self.project = baker.make("projects.Project", organization=self.organization)
        self.project.teams.add(self.team)
        self.list_url = reverse("api:list_projects")
        self.team_list_url = reverse(
            "api:list_team_projects", args=[self.organization.slug, self.team.slug]
        )
        self.detail_url = reverse(
            "api:get_project", args=[self.organization.slug, self.project.slug]
        )

    def test_list(self):
        self.assertGetReqStatusCode(self.list_url, 403)
        self.assertGetReqStatusCode(self.team_list_url, 403)

        self.auth_token.add_permission("project:read")
        self.assertGetReqStatusCode(self.list_url, 200)
        self.assertGetReqStatusCode(self.team_list_url, 200)

    def test_retrieve(self):
        self.assertGetReqStatusCode(self.detail_url, 403)

        self.auth_token.add_permission("project:read")
        self.assertGetReqStatusCode(self.detail_url, 200)

    def test_create(self):
        self.auth_token.add_permission("project:read")
        data = {"name": "new project"}
        self.assertPostReqStatusCode(self.list_url, data, 405)
        self.assertPostReqStatusCode(self.team_list_url, data, 403)

        self.auth_token.add_permission("project:write")
        self.assertPostReqStatusCode(
            self.list_url,
            data,
            405,
            "Post to project endpoint should have no way to select organization",
        )
        self.assertPostReqStatusCode(self.team_list_url, data, 201)

    def test_destroy(self):
        self.auth_token.add_permissions(["project:read", "project:write"])
        self.assertDeleteReqStatusCode(self.detail_url, 403)

        self.auth_token.add_permission("project:admin")
        self.assertDeleteReqStatusCode(self.detail_url, 204)

    def test_user_destroy(self):
        self.set_client_credentials(None)
        self.client.force_login(self.user)
        self.set_user_role(OrganizationUserRole.MEMBER)
        self.assertDeleteReqStatusCode(self.detail_url, 404)

        self.set_user_role(OrganizationUserRole.OWNER)
        self.assertDeleteReqStatusCode(self.detail_url, 204)

    def test_update(self):
        self.auth_token.add_permission("project:read")
        data = {"name": "new name"}
        self.assertPutReqStatusCode(self.detail_url, data, 403)

        self.auth_token.add_permission("project:write")
        self.assertPutReqStatusCode(self.detail_url, data, 200)


class ProjectKeyAPIPermissionTests(APIPermissionTestCase):
    def setUp(self):
        self.create_user_org()
        self.set_client_credentials(self.auth_token.token)
        self.team = baker.make("teams.Team", organization=self.organization)
        self.project = baker.make("projects.Project", organization=self.organization)
        self.project_key = baker.make("projects.ProjectKey", project=self.project)
        self.list_url = reverse(
            "api:list_project_keys", args=[self.organization.slug, self.project.slug]
        )
        self.detail_url = reverse(
            "api:get_project_key",
            args=[
                self.organization.slug,
                self.project.slug,
                self.project_key.public_key,
            ],
        )

    def test_list(self):
        self.assertGetReqStatusCode(self.list_url, 403)
        self.auth_token.add_permission("project:read")
        self.assertGetReqStatusCode(self.list_url, 200)

    def test_retrieve(self):
        self.assertGetReqStatusCode(self.detail_url, 403)
        self.auth_token.add_permission("project:read")
        self.assertGetReqStatusCode(self.detail_url, 200)

    def test_create(self):
        self.auth_token.add_permission("project:read")
        data = {"name": "new project key"}
        self.assertPostReqStatusCode(self.list_url, data, 403)
        self.auth_token.add_permission("project:write")
        self.assertPostReqStatusCode(self.list_url, data, 201)

    def test_destroy(self):
        self.auth_token.add_permissions(["project:read", "project:write"])
        self.assertDeleteReqStatusCode(self.detail_url, 403)
        self.auth_token.add_permission("project:admin")
        self.assertDeleteReqStatusCode(self.detail_url, 204)

    def test_update(self):
        self.auth_token.add_permission("project:read")
        data = {"name": "new label"}
        self.assertPutReqStatusCode(self.detail_url, data, 403)
        self.auth_token.add_permission("project:write")
        self.assertPutReqStatusCode(self.detail_url, data, 200)
