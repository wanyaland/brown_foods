# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='checked_out',
            new_name='active',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='core.Customer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(null=True, upload_to=b'brown_food/%Y/%m/%d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cart',
            name='payment_type',
            field=models.CharField(max_length=100, null=True, choices=[(b'C', b'CASH'), (b'V', b'VISA CARD'), (b'M', b'MOBILE MONEY')]),
        ),
    ]
