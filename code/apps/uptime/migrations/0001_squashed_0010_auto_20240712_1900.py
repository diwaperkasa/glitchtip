# Generated by Django 5.2 on 2025-04-02 19:37

import apps.uptime.migrations.functions.partition
import apps.uptime.models
import datetime
import django.core.validators
import django.db.migrations.operations.special
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import glitchtip.model_utils
import psql_partition.backend.migrations.operations.create_partitioned_model
import psql_partition.manager.manager
import psql_partition.models.partitioned
import psql_partition.types
from django.db import migrations, models


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# apps.uptime.migrations.0009_alter_monitor_interval_alter_monitor_monitor_type_and_more


class Migration(migrations.Migration):
    replaces = [
        ("uptime", "0001_squashed_0008_statuspage_statuspage_unique_organization_slug"),
        ("uptime", "0009_alter_monitor_interval_alter_monitor_monitor_type_and_more"),
        ("uptime", "0010_auto_20240712_1900"),
    ]

    initial = True

    dependencies = [
        (
            "environments",
            "0001_squashed_0003_alter_environment_id_alter_environmentproject_id",
        ),
        (
            "organizations_ext",
            "0001_squashed_0003_alter_organization_id_alter_organization_users_and_more",
        ),
        ("organizations_ext", "0004_organizationsubscription_alter_organization_slug"),
        ("performance", "0014_initial"),
        (
            "projects",
            "0001_squashed_0009_alter_project_id_alter_projectcounter_id_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Monitor",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "monitor_type",
                    models.CharField(
                        choices=[
                            ("Ping", "Ping"),
                            ("GET", "Get"),
                            ("POST", "Post"),
                            ("SSL", "Ssl"),
                            ("Heartbeat", "Heartbeat"),
                        ],
                        default="Ping",
                        max_length=12,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("url", models.URLField(blank=True, max_length=2000)),
                (
                    "expected_status",
                    models.PositiveSmallIntegerField(
                        blank=True, default=200, null=True
                    ),
                ),
                ("expected_body", models.CharField(blank=True, max_length=2000)),
                (
                    "interval",
                    models.DurationField(
                        default=datetime.timedelta(seconds=60),
                        validators=[
                            django.core.validators.MaxValueValidator(
                                datetime.timedelta(days=1)
                            )
                        ],
                    ),
                ),
                (
                    "environment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="environments.environment",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations_ext.organization",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="projects.project",
                    ),
                ),
                (
                    "endpoint_id",
                    models.UUIDField(
                        blank=True,
                        editable=False,
                        help_text="Used for referencing heartbeat endpoint",
                        null=True,
                    ),
                ),
                (
                    "timeout",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Blank implies default value of 20",
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(60),
                            django.core.validators.MinValueValidator(1),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MonitorCheck",
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
                ("is_up", models.BooleanField()),
                (
                    "start_check",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Time when the start of this check was performed",
                    ),
                ),
                (
                    "reason",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (0, "Unknown"),
                            (1, "Timeout"),
                            (2, "Wrong status code"),
                            (3, "Expected response not found"),
                            (4, "SSL error"),
                            (5, "Network error"),
                        ],
                        default=0,
                        null=True,
                    ),
                ),
                ("response_time", models.DurationField(blank=True, null=True)),
                ("data", models.JSONField(blank=True, null=True)),
                (
                    "monitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checks",
                        to="uptime.monitor",
                    ),
                ),
            ],
            options={
                "ordering": ("-start_check",),
                "indexes": [],
            },
        ),
        migrations.AddIndex(
            model_name="monitor",
            index=models.Index(
                fields=["-created"], name="uptime_moni_created_c41912_idx"
            ),
        ),
        migrations.AddField(
            model_name="monitorcheck",
            name="is_change",
            field=models.BooleanField(
                default=False,
                help_text="Indicates change to is_up status for associated monitor",
            ),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name="monitorcheck",
            index=models.Index(
                fields=["monitor", "-start_check"],
                name="uptime_moni_monitor_a89b32_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="monitorcheck",
            index=models.Index(
                fields=["monitor", "is_change", "-start_check"],
                name="uptime_moni_monitor_b6d442_idx",
            ),
        ),
        migrations.CreateModel(
            name="StatusPage",
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
                ("name", models.CharField(max_length=200)),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        max_length=200,
                        populate_from=["name"],
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        help_text="When true, the status page URL is publicly accessible"
                    ),
                ),
                ("monitors", models.ManyToManyField(blank=True, to="uptime.monitor")),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizations_ext.organization",
                    ),
                ),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(
                        fields=("organization", "slug"), name="unique_organization_slug"
                    )
                ],
            },
        ),
        migrations.RenameField(
            model_name="monitor",
            old_name="interval",
            new_name="interval_old",
        ),
        migrations.AddField(
            model_name="monitor",
            name="interval",
            field=models.PositiveSmallIntegerField(
                default=60,
                validators=[
                    django.core.validators.MaxValueValidator(86400),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.RemoveField(
            model_name="monitor",
            name="interval_old",
        ),
        migrations.AlterField(
            model_name="monitor",
            name="monitor_type",
            field=models.CharField(
                choices=[
                    ("Ping", "Ping"),
                    ("GET", "Get"),
                    ("POST", "Post"),
                    ("TCP Port", "Port"),
                    ("SSL", "Ssl"),
                    ("Heartbeat", "Heartbeat"),
                ],
                default="Ping",
                max_length=12,
            ),
        ),
        migrations.AlterField(
            model_name="monitor",
            name="url",
            field=models.CharField(
                blank=True,
                max_length=2000,
                validators=[apps.uptime.models.OptionalSchemeURLValidator()],
            ),
        ),
        migrations.DeleteModel(
            name="MonitorCheck",
        ),
        psql_partition.backend.migrations.operations.create_partitioned_model.PostgresCreatePartitionedModel(
            name="MonitorCheck",
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
                ("is_up", models.BooleanField()),
                (
                    "is_change",
                    models.BooleanField(
                        help_text="Indicates change to is_up status for associated monitor"
                    ),
                ),
                (
                    "start_check",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="Time when the start of this check was performed",
                    ),
                ),
                (
                    "reason",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        choices=[
                            (0, "Unknown"),
                            (1, "Timeout"),
                            (2, "Wrong status code"),
                            (3, "Expected response not found"),
                            (4, "SSL error"),
                            (5, "Network error"),
                        ],
                        default=0,
                        null=True,
                    ),
                ),
                (
                    "response_time",
                    models.PositiveIntegerField(
                        blank=True, help_text="Reponse time in milliseconds", null=True
                    ),
                ),
                ("data", models.JSONField(blank=True, null=True)),
                (
                    "monitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checks",
                        to="uptime.monitor",
                    ),
                ),
            ],
            options={
                "ordering": ("-start_check",),
                "indexes": [
                    models.Index(
                        fields=["monitor", "-start_check"],
                        name="uptime_moni_monitor_a89b32_idx",
                    ),
                    models.Index(
                        fields=["monitor", "is_change", "-start_check"],
                        name="uptime_moni_monitor_b6d442_idx",
                    ),
                ],
            },
            partitioning_options={
                "method": psql_partition.types.PostgresPartitioningMethod["RANGE"],
                "key": ["start_check"],
            },
            bases=(psql_partition.models.partitioned.PostgresPartitionedModel,),
            managers=[
                ("objects", psql_partition.manager.manager.PostgresManager()),
            ],
        ),
        glitchtip.model_utils.TestDefaultPartition(
            model_name="MonitorCheck",
            name="default",
        ),
        migrations.RunPython(
            code=apps.uptime.migrations.functions.partition.create_partitions,
            reverse_code=django.db.migrations.operations.special.RunPython.noop,
        ),
    ]
