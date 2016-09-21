# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160916_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 19, 14, 32, 46, 371000)),
            preserve_default=True,
        ),
    ]
