# Generated by Django 4.0.4 on 2023-03-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bundles', '0012_bundle_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='reward_icon',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='reward icon'),
        ),
    ]