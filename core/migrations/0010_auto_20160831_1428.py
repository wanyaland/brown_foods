# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20160831_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
