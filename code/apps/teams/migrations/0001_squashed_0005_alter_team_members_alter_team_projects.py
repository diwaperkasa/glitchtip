# Generated by Django 5.2 on 2025-04-02 19:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("teams", "0001_squashed_0004_alter_team_id_alter_team_members"),
        ("teams", "0005_alter_team_members_alter_team_projects"),
    ]

    initial = True

    dependencies = [
        (
            "organizations_ext",
            "0001_squashed_0003_alter_organization_id_alter_organization_users_and_more",
        ),
        ("organizations_ext", "0004_organizationsubscription_alter_organization_slug"),
        (
            "projects",
            "0001_squashed_0009_alter_project_id_alter_projectcounter_id_and_more",
        ),
        ("projects", "0015_rename_label_projectkey_name_projectkey_is_active"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("slug", models.SlugField()),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teams",
                        to="organizations_ext.organization",
                    ),
                ),
                (
                    "projects",
                    models.ManyToManyField(related_name="teams", to="projects.project"),
                ),
                (
                    "members",
                    models.ManyToManyField(
                        blank=True,
                        related_name="teams",
                        to="organizations_ext.organizationuser",
                    ),
                ),
            ],
            options={
                "unique_together": {("slug", "organization")},
            },
        ),
        migrations.RunSQL(
            sql="\nCREATE OR REPLACE FUNCTION check_teamproject_organization() RETURNS TRIGGER AS $$\nBEGIN\n    IF NEW.team_id IS NOT NULL AND NEW.project_id IS NOT NULL THEN\n        PERFORM 1\n        FROM projects_project p\n        JOIN teams_team t ON t.organization_id = p.organization_id\n        WHERE p.id = NEW.project_id AND t.id = NEW.team_id;\n        IF NOT FOUND THEN\n            RAISE EXCEPTION 'Team and Project must belong to the same organization';\n        END IF;\n    END IF;\n    RETURN NEW;\nEND;\n$$ LANGUAGE plpgsql;\n\nDROP TRIGGER IF EXISTS check_teamproject_organization_trigger ON teams_team_projects;\nCREATE TRIGGER check_teamproject_organization_trigger\nBEFORE INSERT OR UPDATE ON teams_team_projects\nFOR EACH ROW EXECUTE FUNCTION check_teamproject_organization();\n\n",
            reverse_sql="",
        ),
    ]
