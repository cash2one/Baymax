# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wp_bug',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wp_module',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wp_permission',
            },
        ),
        migrations.CreateModel(
            name='PermissionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wp_permissiontype',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wp_product',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wp_producttype',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wp_role',
            },
        ),
        migrations.CreateModel(
            name='Role_Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission', models.ForeignKey(to='woodpecker.Permission')),
                ('role', models.ForeignKey(to='woodpecker.Role')),
            ],
            options={
                'db_table': 'wp_role_permission',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('product', models.ForeignKey(to='woodpecker.Product')),
            ],
            options={
                'db_table': 'wp_task',
            },
        ),
        migrations.CreateModel(
            name='Task_TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.ForeignKey(to='woodpecker.Task')),
            ],
            options={
                'db_table': 'wp_result',
            },
        ),
        migrations.CreateModel(
            name='Task_TestCase_Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bug', models.ForeignKey(to='woodpecker.Bug')),
                ('task', models.ForeignKey(to='woodpecker.Task')),
            ],
            options={
                'db_table': 'wp_result_bug',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'wp_team',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('module', models.ForeignKey(to='woodpecker.Module')),
            ],
            options={
                'db_table': 'wp_testcase',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('true_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('team', models.ForeignKey(to='woodpecker.Team')),
            ],
            options={
                'db_table': 'wp_user',
            },
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.ForeignKey(to='woodpecker.Role')),
                ('user', models.ForeignKey(to='woodpecker.User')),
            ],
            options={
                'db_table': 'wp_user_role',
            },
        ),
        migrations.AddField(
            model_name='testcase',
            name='user',
            field=models.ForeignKey(to='woodpecker.User'),
        ),
        migrations.AddField(
            model_name='task_testcase_bug',
            name='testcase',
            field=models.ForeignKey(to='woodpecker.TestCase'),
        ),
        migrations.AddField(
            model_name='task_testcase',
            name='testcase',
            field=models.ForeignKey(to='woodpecker.TestCase'),
        ),
        migrations.AddField(
            model_name='task',
            name='testcases',
            field=models.ManyToManyField(to='woodpecker.TestCase', through='woodpecker.Task_TestCase'),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(to='woodpecker.User'),
        ),
        migrations.AddField(
            model_name='role',
            name='Users',
            field=models.ManyToManyField(to='woodpecker.User', through='woodpecker.User_Role'),
        ),
        migrations.AddField(
            model_name='product',
            name='team',
            field=models.ForeignKey(to='woodpecker.Team'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(to='woodpecker.ProductType'),
        ),
        migrations.AddField(
            model_name='permission',
            name='roles',
            field=models.ManyToManyField(to='woodpecker.Role', through='woodpecker.Role_Permission'),
        ),
        migrations.AddField(
            model_name='permission',
            name='type',
            field=models.ForeignKey(to='woodpecker.PermissionType'),
        ),
        migrations.AddField(
            model_name='module',
            name='product',
            field=models.ForeignKey(to='woodpecker.Product'),
        ),
        migrations.AddField(
            model_name='bug',
            name='tasks',
            field=models.ManyToManyField(to='woodpecker.Task', through='woodpecker.Task_TestCase_Bug'),
        ),
        migrations.AddField(
            model_name='bug',
            name='testcases',
            field=models.ManyToManyField(to='woodpecker.TestCase', through='woodpecker.Task_TestCase_Bug'),
        ),
        migrations.AlterUniqueTogether(
            name='user_role',
            unique_together=set([('user', 'role')]),
        ),
        migrations.AlterUniqueTogether(
            name='task_testcase_bug',
            unique_together=set([('task', 'testcase', 'bug')]),
        ),
        migrations.AlterUniqueTogether(
            name='task_testcase',
            unique_together=set([('task', 'testcase')]),
        ),
        migrations.AlterUniqueTogether(
            name='role_permission',
            unique_together=set([('role', 'permission')]),
        ),
    ]
