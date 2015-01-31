from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate
import util
import json


@csrf_exempt
def add_user(request):
    if request.method == "GET":
        return HttpResponse(status=400)

    username = request.POST['username']
    token = request.POST['token']

    new_user = None

    try:
        new_user = User.objects.create_user(username, "", token)
        user1 = UserProfile(user=new_user)
    except Exception as e:
        if new_user:
            new_user.delete()
        response_data = {'error': "username already exists"}
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)

    user1.save()
    response_data = {'error': "none"}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def new_bathroom(request):
    return


def upload_photo(request):
    return


def new_user(request):
    return


def add_review(request):
    return


def new_bathroom(request):
    return


def check_in(request):
    return


def add_rating(request):
    return


def heart_bathroom(request):
    return


def like_review(request):
    return


def get_nearby_bathrooms(request):
    if request.method == "GET":
        return HttpResponse(status=400)
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']



