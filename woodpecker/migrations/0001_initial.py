# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('department', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bug',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'module',
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
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='PermissionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'permissiontype',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'producttype',
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
                'db_table': 'role',
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
                'db_table': 'role_permission',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.IntegerField(default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(to='woodpecker.Product')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='Task_TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('task', models.ForeignKey(to='woodpecker.Task')),
            ],
            options={
                'db_table': 'result',
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
                'db_table': 'result_bug',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('module', models.ForeignKey(to='woodpecker.Module')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'testcase',
            },
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.ForeignKey(to='woodpecker.Role')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_role',
            },
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='role',
            name='Users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='woodpecker.User_Role'),
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
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(to='woodpecker.Team'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
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
