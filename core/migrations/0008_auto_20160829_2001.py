# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20160827_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='email',
            field=models.EmailField(max_length=75, null=True),
        ),
    ]
