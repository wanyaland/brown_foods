# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20160923_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='delivery',
        ),
        migrations.AddField(
            model_name='cart',
            name='delivery',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 23, 13, 12, 1, 986000)),
        ),
    ]
