# Generated by Django 4.0.4 on 2023-03-09 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bundles', '0013_bundle_reward_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('icon', models.CharField(blank=True, max_length=50, null=True, verbose_name='icon')),
            ],
        ),
        migrations.RemoveField(
            model_name='bundle',
            name='reward_icon',
        ),
        migrations.AlterField(
            model_name='bundle',
            name='reward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bundles.reward'),
        ),
    ]
