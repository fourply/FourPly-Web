# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unchained', '0002_auto_20150201_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='uid',
            field=models.CharField(default=b'10b8a4c8-f97d-4625-bf20-5bc550626625', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 2, 1, 0, 17, 55, 937932)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='check_ins',
            field=models.ManyToManyField(related_name='check_ins', to='unchained.Bathroom'),
            preserve_default=True,
        ),
    ]
