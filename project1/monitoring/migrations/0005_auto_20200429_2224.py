# Generated by Django 3.0.5 on 2020-04-29 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0004_auto_20200429_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='probe',
            name='probegroup',
        ),
        migrations.AddField(
            model_name='probe',
            name='probegroup',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitoring.Group'),
        ),
    ]
