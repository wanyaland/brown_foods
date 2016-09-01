# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20160829_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='address_line1',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='address_line2',
            field=models.TextField(null=True),
        ),
    ]
