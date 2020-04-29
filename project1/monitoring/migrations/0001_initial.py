# Generated by Django 3.0.5 on 2020-04-29 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DashboardGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_dashboardgroup', to='monitoring.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('code', models.CharField(blank=True, max_length=60)),
                ('description', models.TextField(blank=True, null=True)),
                ('groupdashboard', models.ManyToManyField(through='monitoring.DashboardGroup', to='monitoring.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('ipaddr', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Probe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('path', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProbeHostStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='probe_group', to='monitoring.Group')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probe_host', to='monitoring.Host')),
                ('probe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='probe_probe', to='monitoring.Probe')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='probe_status', to='monitoring.Status')),
            ],
        ),
        migrations.AddField(
            model_name='probe',
            name='probehost',
            field=models.ManyToManyField(through='monitoring.ProbeHostStatus', to='monitoring.Host'),
        ),
        migrations.AddField(
            model_name='probe',
            name='probestatus',
            field=models.ManyToManyField(through='monitoring.ProbeHostStatus', to='monitoring.Status'),
        ),
        migrations.AddField(
            model_name='dashboardgroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dashboard_group', to='monitoring.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='dashboardgroup',
            unique_together={('dashboard', 'group')},
        ),
    ]
