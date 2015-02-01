# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unchained', '0004_auto_20150201_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroom',
            name='uid',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 2, 1, 0, 59, 1, 364140)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_uid',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
