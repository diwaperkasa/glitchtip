# Generated by Django 4.1 on 2022-08-18 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("performance", "0008_transactionevent_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="span",
            name="description",
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
