# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150310_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemodule',
            name='Description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
