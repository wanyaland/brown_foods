# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20160923_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address_line1',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='address_line2',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 24, 2, 0, 32, 533000)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
