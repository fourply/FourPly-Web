from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import uuid


class Bathroom(models.Model):
    uid = models.CharField(max_length=128)
    name = models.CharField(max_length=30)
    rating = models.DecimalField(decimal_places=2, max_digits=4,default=0)
    num_ratings = models.IntegerField(default=0, max_length=128)
    total_ratings = models.IntegerField(default=0, max_length=128)
    num_visitors = models.IntegerField(default=0)
    num_hearts = models.IntegerField(default=0)
    has_twoply = models.BooleanField(default=False)
    lat = models.DecimalField(decimal_places=6, max_digits=9)
    lon = models.DecimalField(decimal_places=6, max_digits=9)

    def __unicode__(self):
        return 'Bathroom: {0}\n \
                rating: {1}\n \
                total visitors: {2}\n \
                hearts: {3} \n \
                has two ply?: {4}\n \
                lat: {5}\n \
                lon: {6}\n \
                uid: {7}\n \
                '.format(self.name, self.rating, self.num_visitors, self.num_hearts, self.has_twoply, self.lat, self.lon, self.uid)


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
    check_ins = models.ManyToManyField(Bathroom,related_name="check_ins")
    liked_reviews = models.ManyToManyField(Review)
    hearts = models.ManyToManyField(Bathroom,related_name="hearts")

    def __unicode__(self):
        return "%s's Profile" % self.user.username


