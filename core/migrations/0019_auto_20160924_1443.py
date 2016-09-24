# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20160924_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 24, 14, 43, 50, 613000)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='payment_type',
            field=models.CharField(max_length=100, null=True, choices=[(b'Pre', b'PREPAID'), (b'Post', b'POSTPAID')]),
        ),
    ]
