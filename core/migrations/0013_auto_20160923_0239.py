# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20160923_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='customer',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 23, 2, 39, 41, 768000)),
        ),
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2),
        ),
    ]
