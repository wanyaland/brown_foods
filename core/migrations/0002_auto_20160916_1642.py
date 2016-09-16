# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_type',
            field=models.CharField(max_length=100, null=True, choices=[(b'M', b'MAIN'), (b'S', b'SIDE DISH')]),
            preserve_default=True,
        ),
    ]
