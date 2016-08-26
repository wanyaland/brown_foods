# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20160825_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('address_line1', models.TextField()),
                ('address_line2', models.TextField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('phone_number', models.CharField(max_length=20)),
                ('order_notes', models.TextField()),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(to='core.Cart')),
                ('menu_item', models.ForeignKey(to='core.MenuItem')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu_item',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='active',
            new_name='checked_out',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='order_date',
            new_name='creation_date',
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='core.BillingDetails', null=True),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
