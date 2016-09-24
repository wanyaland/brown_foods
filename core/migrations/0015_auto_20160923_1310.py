# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20160923_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='delivery',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 23, 13, 10, 54, 55000)),
        ),
    ]
