# Generated by Django 3.0.3 on 2020-02-28 17:52

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations_ext', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name', 'organization_id'])),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('platform', models.CharField(blank=True, max_length=64, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='organizations_ext.Organization')),
            ],
            options={
                'unique_together': {('organization', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProjectKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=64)),
                ('public_key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rate_limit_count', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rate_limit_window', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]