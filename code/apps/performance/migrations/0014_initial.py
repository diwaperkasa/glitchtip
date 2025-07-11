# Generated by Django 5.0.7 on 2024-07-12 14:55

import django.contrib.postgres.search
import django.db.models.deletion
import psql_partition.backend.migrations.operations.add_default_partition
import psql_partition.backend.migrations.operations.create_partitioned_model
import psql_partition.manager.manager
import psql_partition.models.partitioned
import psql_partition.types
import uuid
from django.db import migrations, models
from glitchtip.model_utils import TestDefaultPartition


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("performance", "0013_alter_transactionevent_options_and_more"),
        ("projects", "0015_rename_label_projectkey_name_projectkey_is_active"),
    ]

    operations = [
        psql_partition.backend.migrations.operations.create_partitioned_model.PostgresCreatePartitionedModel(
            name="TransactionEvent",
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
                ("trace_id", models.UUIDField(db_index=True)),
                (
                    "start_timestamp",
                    models.DateTimeField(
                        db_index=True,
                        help_text="Datetime reported by client as the time the measurement started",
                    ),
                ),
                (
                    "timestamp",
                    models.DateTimeField(
                        blank=True,
                        help_text="Datetime reported by client as the time the measurement finished",
                        null=True,
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        db_index=True, help_text="Milliseconds"
                    ),
                ),
                (
                    "data",
                    models.JSONField(help_text="General event data that is searchable"),
                ),
                ("tags", models.JSONField(default=dict)),
            ],
            options={
                "ordering": ["-start_timestamp"],
            },
            partitioning_options={
                "method": psql_partition.types.PostgresPartitioningMethod["RANGE"],
                "key": ["start_timestamp"],
            },
            bases=(psql_partition.models.partitioned.PostgresPartitionedModel,),
            managers=[
                ("objects", psql_partition.manager.manager.PostgresManager()),
            ],
        ),
        TestDefaultPartition(
            model_name="TransactionEvent",
            name="default",
        ),
        migrations.CreateModel(
            name="TransactionGroup",
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
                ("transaction", models.CharField(max_length=1024)),
                ("op", models.CharField(max_length=255)),
                ("method", models.CharField(blank=True, max_length=255, null=True)),
                ("tags", models.JSONField(default=dict)),
                (
                    "search_vector",
                    django.contrib.postgres.search.SearchVectorField(
                        editable=False, null=True
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projects.project",
                    ),
                ),
            ],
            options={
                "unique_together": {("transaction", "project", "op", "method")},
            },
        ),
        migrations.AddField(
            model_name="transactionevent",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="performance.transactiongroup",
            ),
        ),
    ]
