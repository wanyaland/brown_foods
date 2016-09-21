# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('address_line1', models.TextField(null=True)),
                ('address_line2', models.TextField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('order_notes', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation_date', models.DateTimeField(null=True)),
                ('checked_out', models.BooleanField(default=False)),
                ('payment_type', models.CharField(max_length=100, null=True, choices=[(b'C', b'CASH'), (b'V', b'VISA CARD'), (b'M', b'MOBILE MONEY')])),
                ('payment_id', models.CharField(max_length=20, null=True)),
                ('billing_details', models.OneToOneField(null=True, to='core.BillingDetails')),
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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=b'brown_food/%Y/%m/%d')),
                ('unit_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100, choices=[(b'M', b'MAIN'), (b'S', b'SIDE DISH')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='menu_item',
            field=models.ForeignKey(to='core.MenuItem'),
            preserve_default=True,
        ),
    ]
