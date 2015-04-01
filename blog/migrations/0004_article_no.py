# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150331_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='No',
            field=models.CharField(default=123333, max_length=20),
            preserve_default=False,
        ),
    ]
