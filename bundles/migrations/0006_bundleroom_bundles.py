# Generated by Django 4.0.4 on 2023-03-06 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bundles", "0005_alter_bundleitem_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="bundleroom",
            name="bundles",
            field=models.ManyToManyField(blank=True, to="bundles.bundle"),
        ),
    ]