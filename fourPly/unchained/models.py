from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import uuid


class Bathroom(models.Model):
    uid = models.CharField(max_length=128, default=str(uuid.uuid4()))
    name = models.CharField(max_length=30)
    rating = models.DecimalField(decimal_places=2,max_digits=4,default=0)
    num_visitors = models.IntegerField(default=0)
    num_hearts = models.IntegerField(default=0)
    has_twoply = models.BooleanField(default=False)
    lat = models.DecimalField(decimal_places=6, max_digits=9)
    lon = models.DecimalField(decimal_places=6, max_digits=9)


class Photo(models.Model):
    uri = models.CharField(max_length=128)


class Review(models.Model):
    bathroom = models.ForeignKey(Bathroom)
    author = models.CharField(max_length=128)
    date_created = models.DateField(default=datetime.now())
    message = models.TextField(default="")
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                        MaxValueValidator(5)])


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_uid = models.CharField(max_length=128)
    token = models.CharField(max_length=128)
    check_ins = models.ManyToManyField(Bathroom)
    liked_reviews = models.ManyToManyField(Review)
    hearts = models.ManyToManyField(Bathroom)


