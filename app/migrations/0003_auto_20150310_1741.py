# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150309_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='IsShared',
            field=models.BooleanField(default=1),
            preserve_default=True,
        ),
    ]
