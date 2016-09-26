# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20160926_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='delivery',
        ),
        migrations.AddField(
            model_name='billingdetails',
            name='address_line3',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='self_collect',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 26, 17, 51, 26, 280000)),
        ),
    ]
