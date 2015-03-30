# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woodpecker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='CreateWay',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='DeviceType',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
