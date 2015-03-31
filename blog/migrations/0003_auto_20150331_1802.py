# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('TagName', models.CharField(max_length=50)),
                ('ArticleId', models.ForeignKey(to='blog.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='article',
            old_name='Property',
            new_name='Status',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Property',
            new_name='Status',
        ),
    ]
