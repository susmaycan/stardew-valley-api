# Generated by Django 4.0.4 on 2023-03-09 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bundles", "0010_delete_season_alter_bundleitem_season"),
    ]

    operations = [
        migrations.AddField(
            model_name="bundle",
            name="image",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="image"
            ),
        ),
        migrations.AddField(
            model_name="bundleitem",
            name="image",
            field=models.CharField(
                blank=True, max_length=200, null=True, verbose_name="image"
            ),
        ),
    ]
