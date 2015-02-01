# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('unchained', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroom',
            name='uid',
            field=models.CharField(default=b'b40f53a1-6047-4bb9-83f4-736a391e3720', max_length=128),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='review',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2015, 2, 1, 0, 10, 22, 350874)),
            preserve_default=True,
        ),
    ]
