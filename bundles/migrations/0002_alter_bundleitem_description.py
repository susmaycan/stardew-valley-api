# Generated by Django 4.0.4 on 2023-03-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bundles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bundleitem",
            name="description",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="description"
            ),
        ),
    ]
