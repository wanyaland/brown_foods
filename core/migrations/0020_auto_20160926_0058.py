# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20160924_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 26, 0, 58, 11, 59000)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_postpaid',
            field=models.BooleanField(default=False),
        ),
    ]
