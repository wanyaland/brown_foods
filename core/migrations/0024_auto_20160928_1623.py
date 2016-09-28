# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20160927_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 28, 16, 23, 19, 384000)),
        ),
        migrations.AlterField(
            model_name='cart',
            name='payment_type',
            field=models.CharField(max_length=100, null=True, choices=[(b'Pre', b'PREPAID'), (b'Post', b'POSTPAID'), (b'Self', b'SELF_COLLECTS')]),
        ),
    ]
