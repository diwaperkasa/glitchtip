# Generated by Django 5.2.1 on 2025-05-24 16:19

import django.contrib.postgres.fields
import django.contrib.postgres.indexes
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueevent',
            name='hashes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), db_default=[], size=None),
        ),
        migrations.AddIndex(
            model_name='issueevent',
            index=django.contrib.postgres.indexes.GinIndex(fields=['hashes'], name='issue_event_hashes_eedb7c_gin'),
        ),
    ]
