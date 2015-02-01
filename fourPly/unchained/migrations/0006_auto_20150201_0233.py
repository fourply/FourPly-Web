# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unchained', '0005_auto_20150201_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bathroom',
            old_name='total_ratings',
            new_name='total_rating',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='liked_reviews',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='ratings',
            field=models.ManyToManyField(related_name='ratings', to='unchained.Bathroom'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 2, 1, 2, 33, 10, 552868)),
            preserve_default=True,
        ),
    ]
