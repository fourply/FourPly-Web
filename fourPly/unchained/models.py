from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Model


class Bathroom(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    rating = models.DecimalField(decimal_places=2)
    other_people = models.IntegerField()
    lat = models.DecimalField()
    lon = models.DecimalField()


class Photo(models.Model):
    uri = models.CharField(max_length=128)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField()
    check_ins = models.ManyToManyField(Bathroom)

