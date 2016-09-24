# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160920_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='PesaPal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracking_id', models.CharField(max_length=50, verbose_name=b'Pesapal Tracking id')),
                ('reference', models.CharField(max_length=50, verbose_name=b'Pesapal reference number')),
                ('status', models.CharField(default=b'PENDING', max_length=10, choices=[(b'PENDING', b'Pending'), (b'COMPLETED', b'Completed'), (b'FAILED', b'Failed'), (b'INVALID', b'Invalid')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='billingdetails',
            name='delivery_date',
            field=models.DateField(default=datetime.datetime(2016, 9, 22, 15, 46, 43, 716000)),
        ),
    ]
