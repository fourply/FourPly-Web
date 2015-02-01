# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(default=b'86bc7c5a-acdd-4b2d-9943-05bff37ef769', max_length=128)),
                ('name', models.CharField(max_length=30)),
                ('rating', models.DecimalField(default=0, max_digits=4, decimal_places=2)),
                ('num_ratings', models.IntegerField(default=0, max_length=128)),
                ('total_ratings', models.IntegerField(default=0, max_length=128)),
                ('num_visitors', models.IntegerField(default=0)),
                ('num_hearts', models.IntegerField(default=0)),
                ('has_twoply', models.BooleanField(default=False)),
                ('lat', models.DecimalField(max_digits=9, decimal_places=6)),
                ('lon', models.DecimalField(max_digits=9, decimal_places=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=128)),
                ('date_created', models.DateField(default=datetime.datetime(2015, 2, 1, 0, 9, 38, 432757))),
                ('message', models.TextField(default=b'')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('bathroom', models.ForeignKey(to='unchained.Bathroom')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_uid', models.CharField(max_length=128)),
                ('token', models.CharField(max_length=128)),
                ('check_ins', models.ManyToManyField(related_name='check_in', to='unchained.Bathroom')),
                ('hearts', models.ManyToManyField(related_name='hearts', to='unchained.Bathroom')),
                ('liked_reviews', models.ManyToManyField(to='unchained.Review')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
