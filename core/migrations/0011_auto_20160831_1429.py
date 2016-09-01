# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20160831_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='order_notes',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='phone_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
