# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20160927_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='delivery_date',
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 27, 2, 34, 27, 489000)),
        ),
    ]
