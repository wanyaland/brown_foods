# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20160926_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivery_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 27, 2, 33, 32, 855000)),
        ),
    ]
