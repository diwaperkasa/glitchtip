# Generated by Django 3.1.5 on 2021-01-17 17:07

import django.contrib.postgres.fields.hstore
import django.contrib.postgres.operations
from django.db import migrations, models
import django.db.models.deletion
import uuid
from issues.migrations.sql.triggers import UPDATE_ISSUE_TRIGGER


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("issues", "0001_squashed_0010_auto_20210117_1543"),
        ("releases", "0002_auto_20201227_1518"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Event",
                    fields=[
                        (
                            "event_id",
                            models.UUIDField(
                                default=uuid.uuid4,
                                editable=False,
                                primary_key=True,
                                serialize=False,
                            ),
                        ),
                        (
                            "timestamp",
                            models.DateTimeField(
                                blank=True,
                                help_text="Date created as claimed by client it came from",
                                null=True,
                            ),
                        ),
                        (
                            "created",
                            models.DateTimeField(auto_now_add=True, db_index=True),
                        ),
                        ("data", models.JSONField()),
                        (
                            "issue",
                            models.ForeignKey(
                                help_text="Sentry calls this a group",
                                on_delete=django.db.models.deletion.CASCADE,
                                to="issues.issue",
                            ),
                        ),
                        (
                            "release",
                            models.ForeignKey(
                                blank=True,
                                null=True,
                                on_delete=django.db.models.deletion.SET_NULL,
                                to="releases.release",
                            ),
                        ),
                        (
                            "tags",
                            models.ManyToManyField(blank=True, to="events.EventTag"),
                        ),
                    ],
                    options={
                        "ordering": ["-created"],
                    },
                ),
                migrations.CreateModel(
                    name="EventTagKey",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("key", models.CharField(max_length=255, unique=True)),
                    ],
                ),
                migrations.CreateModel(
                    name="EventTag",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("value", models.CharField(max_length=225)),
                        (
                            "key",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.CASCADE,
                                to="events.eventtagkey",
                            ),
                        ),
                    ],
                    options={
                        "unique_together": {("key", "value")},
                    },
                ),
            ],
        ),
        migrations.RunSQL(
            sql=UPDATE_ISSUE_TRIGGER,
            reverse_sql="DROP TRIGGER IF EXISTS event_issue_update on issues_event; DROP FUNCTION IF EXISTS update_issue;",
        ),
        migrations.AlterField(
            model_name="event",
            name="issue",
            field=models.ForeignKey(
                help_text="Sentry calls this a group",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="issues.issue",
            ),
        ),
        migrations.RemoveField(
            model_name="event",
            name="tags",
        ),
        django.contrib.postgres.operations.HStoreExtension(),
        migrations.AddField(
            model_name="event",
            name="tags",
            field=django.contrib.postgres.fields.hstore.HStoreField(default=dict),
        ),
        migrations.DeleteModel(
            name="EventTag",
        ),
        migrations.DeleteModel(
            name="EventTagKey",
        ),
    ]
