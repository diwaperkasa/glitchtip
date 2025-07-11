# Generated by Django 5.1.5 on 2025-02-06 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("files", "0009_alter_file_size"),
        (
            "organizations_ext",
            "0007_rename_stripe_subscription_id_organization_stripe_customer_id",
        ),
        ("sourcecode", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="debugsymbolbundle",
            name="file",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="files.file"
            ),
        ),
        migrations.AlterField(
            model_name="debugsymbolbundle",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="organizations_ext.organization",
            ),
        ),
    ]
