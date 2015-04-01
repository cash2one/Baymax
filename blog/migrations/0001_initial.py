# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('No', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=150)),
                ('PostTime', models.DateTimeField(auto_now_add=True)),
                ('UpdateTime', models.DateTimeField(auto_now=True)),
                ('Content', models.TextField(null=True, blank=True)),
                ('ReplyNum', models.IntegerField(default=0)),
                ('ReadNum', models.IntegerField(default=0)),
                ('Status', models.IntegerField(default=0)),
                ('Description', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TypeName', models.CharField(max_length=50)),
                ('TypeDescription', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NickName', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Content', models.TextField(null=True, blank=True)),
                ('ReplyContent', models.TextField(null=True, blank=True)),
                ('ReplyTime', models.DateTimeField()),
                ('FromIp', models.CharField(max_length=20, null=True, blank=True)),
                ('Status', models.IntegerField(default=0)),
                ('CreateTime', models.DateTimeField()),
                ('ArticleId', models.ForeignKey(to='blog.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TagName', models.CharField(max_length=50)),
                ('Quote', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagsMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ArticleId', models.ForeignKey(to='blog.ArticleType')),
                ('TagsId', models.ForeignKey(to='blog.Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='ArticleTypeId',
            field=models.ForeignKey(to='blog.ArticleType'),
            preserve_default=True,
        ),
    ]
