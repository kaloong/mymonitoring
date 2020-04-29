# Generated by Django 3.0.5 on 2020-04-29 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_group_groupprobe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='groupprobe',
        ),
        migrations.AddField(
            model_name='group',
            name='groupprobe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.Probe'),
        ),
    ]
