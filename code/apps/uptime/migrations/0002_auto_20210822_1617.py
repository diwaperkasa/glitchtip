# Generated by Django 3.2.6 on 2021-08-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("uptime", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="monitor",
            name="endpoint_id",
            field=models.UUIDField(
                blank=True,
                editable=False,
                help_text="Used for referencing heartbeat endpoint",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="monitorcheck",
            name="reason",
            field=models.PositiveSmallIntegerField(
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
    ]
