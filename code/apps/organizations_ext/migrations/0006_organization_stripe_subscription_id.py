# Generated by Django 5.1.5 on 2025-02-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizations_ext", "0005_organization_event_throttle_rate"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="stripe_subscription_id",
            field=models.CharField(blank=True, max_length=28),
        ),
    ]
