from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import uuid


class Bathroom(models.Model):
    uid = models.CharField(max_length=128, primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=30, primary_key=True)
    rating = models.DecimalField(decimal_places=2)
    num_visitors = models.IntegerField()
    num_hearts = models.IntegerField(default=0)
    has_twoply = models.BooleanField(default=False)
    lat = models.DecimalField()
    lon = models.DecimalField()


class Photo(models.Model):
    uri = models.CharField(max_length=128)


class UserProfile(models.Model):
    user_id = models.CharField(max_length=128, primary_key=True)
    user = models.OneToOneField(User)
    token = models.CharField(max_length=128)
    check_ins = models.ManyToManyField(Bathroom)
    liked_reviews = models.ManyToManyField(Review)


class Review(models.Model):
    bathroom = models.ForeignKey(Bathroom)
    author = models.CharField(max_length=128)
    date_created = models.DateField(default=datetime.now())
    message = models.TextField()
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0),
                                                        MaxValueValidator(5)])
