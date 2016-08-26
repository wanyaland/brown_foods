# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160825_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False),
        ),
    ]
