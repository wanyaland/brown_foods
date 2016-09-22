# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160922_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesapal',
            name='cart',
            field=models.OneToOneField(null=True, to='core.Cart'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 22, 16, 39, 50, 257000)),
        ),
    ]
