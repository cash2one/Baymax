# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UserName', models.CharField(max_length=50)),
                ('DisplayName', models.CharField(max_length=50)),
                ('UserPassword', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100, blank=True)),
                ('UserDefined', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DeviceModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ModuleName', models.CharField(max_length=300)),
                ('DisplayName', models.CharField(max_length=300)),
                ('IsEnable', models.BooleanField(default=True)),
                ('CreateTime', models.DateTimeField(null=True)),
                ('UpdateTime', models.DateTimeField(null=True)),
                ('Description', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DeviceId', models.CharField(max_length=50, blank=True)),
                ('TestResult', models.TextField(blank=True)),
                ('StartTime', models.DateTimeField(blank=True)),
                ('EndTime', models.DateTimeField(blank=True)),
                ('TestResultFile', models.CharField(max_length=50)),
                ('ResultCount', models.IntegerField()),
                ('ValueSettings', models.TextField(blank=True)),
                ('IsEnable', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TaskName', models.CharField(max_length=50)),
                ('TaskType', models.IntegerField(default=0)),
                ('TaskCount', models.IntegerField()),
                ('TaskState', models.IntegerField()),
                ('DeviceType', models.CharField(max_length=50)),
                ('Description', models.TextField(blank=True)),
                ('CreateTime', models.DateTimeField()),
                ('UpdateTime', models.DateTimeField()),
                ('CreateWay', models.CharField(max_length=50)),
                ('IsShared', models.BooleanField(default=False)),
                ('Creator', models.ForeignKey(to='app.AppUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TestCaseName', models.CharField(max_length=50)),
                ('DisplayName', models.CharField(max_length=50)),
                ('ExecuteCount', models.IntegerField()),
                ('ActivityValue', models.TextField(blank=True)),
                ('TestCaseAction', models.CharField(max_length=100, blank=True)),
                ('TestCaseEntity', models.CharField(max_length=100, blank=True)),
                ('IsEnable', models.BooleanField(default=True)),
                ('CreateTime', models.DateTimeField(null=True)),
                ('UpdateTime', models.DateTimeField(null=True)),
                ('Description', models.TextField(blank=True)),
                ('AloneUse', models.CharField(max_length=50, blank=True)),
                ('IsJoin', models.BooleanField(default=True)),
                ('ModuleId', models.ForeignKey(to='app.DeviceModule')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='result',
            name='TaskId',
            field=models.ForeignKey(to='app.Task'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='TestCaseId',
            field=models.ForeignKey(to='app.TestCase'),
            preserve_default=True,
        ),
    ]
