# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20160923_0239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingdetails',
            name='order_notes',
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 23, 2, 46, 51, 316000)),
        ),
    ]
