# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160919_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='content',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 20, 2, 55, 13, 922000)),
        ),
    ]
