from django.test import TestCase
from django.urls import reverse
from model_bakery import baker

from apps.organizations_ext.models import OrganizationUserRole

from ..models import ProjectKey


class ProjectKeyAPITestCase(TestCase):
    def setUp(self):
        self.user = baker.make("users.user")
        self.client.force_login(self.user)
        self.organization = baker.make("organizations_ext.Organization")
        self.organization.add_user(self.user, role=OrganizationUserRole.OWNER)
        self.project = baker.make("projects.Project", organization=self.organization)
        self.url = reverse(
            "api:list_project_keys", args=[self.organization.slug, self.project.slug]
        )

    def test_key_dsn(self):
        project_key = ProjectKey.objects.get()
        res = self.client.get(self.url)
        self.assertContains(res, project_key.public_key_hex)
