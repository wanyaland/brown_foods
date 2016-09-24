# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160922_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='is_postpaid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 23, 1, 19, 52, 721000)),
        ),
    ]
