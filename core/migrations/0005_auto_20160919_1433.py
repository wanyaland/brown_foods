# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_billingdetails_delivery_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='phone_number2',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 19, 14, 33, 54, 42000)),
        ),
    ]
