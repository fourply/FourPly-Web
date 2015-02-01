# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unchained', '0003_auto_20150201_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='token',
        ),
        migrations.AlterField(
            model_name='bathroom',
            name='uid',
            field=models.CharField(default=b'bb26f3c0-4273-4574-adb4-c570fd26e3fa', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 2, 1, 0, 51, 0, 131991)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_uid',
            field=models.CharField(default=b'd57cbbd9-f733-42a9-a3bb-d691cd067e54', max_length=128),
            preserve_default=True,
        ),
    ]
