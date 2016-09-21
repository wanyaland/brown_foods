# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160916_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(null=True, upload_to=b'brown_food/%Y/%m/%d', blank=True),
        ),
    ]
