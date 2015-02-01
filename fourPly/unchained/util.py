import math
from .models import UserProfile
from django.contrib.auth import authenticate
import json
from django.http import HttpResponse


def auth_user(request):
    """

    :param request: request containing an username and token
    :return: users profile or none if error
    """
    username = request.POST.get('username')
    password = request.POST.get('token')
    if (not username) or (not password):
        return None
    user = authenticate(username=username, password=password)
    if user:
        profile = UserProfile.objects.get(user=user)
        return profile
    else:
        return None


def get_post_args(request,args):
    values = []
    for arg in args:
        values.append(request.POST[arg])
    if len(values) == 1:
        return values[0]
    else:
        return values


def bad_request(error):
    response_data = {'error': error}
    return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)


def auth_failed():
    response_data = {'error': "authentication failed"}
    return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)


def is_nearby(location1, location2, default_threshold=.4):
    """
    Return True or False if two latitude longitude tuples are relatively
    close to each other. 
    Input a default_threshold in kilometers.
    
    >>> a = (34.410977, -119.847042)
    >>> freebirds = (34.413283, -119.855612)
    >>> lagoon = (34.411583, -119.849765)
    >>> is_nearby(a, freebirds)
    False
    >>> is_nearby(a, lagoon)
    True
    >>> is_nearby(lagoon, freebirds)
    False
    """
    lat1, lon1 = location1
    lat2, lon2 = location2

    # Radius of the earth in km
    radius = 6378.137

    lat = deg_rad(lat1-lat2)
    lon = deg_rad(lon1-lon2)

    h = math.sin(lat/2)**2 + math.cos(deg_rad(lat1)) * math.cos(deg_rad(lat2)) * math.sin(lon/2)**2
    i = 2 * math.atan2(math.sqrt(h), math.sqrt(1-h))
    return i * radius < default_threshold

def deg_rad(degrees):
    """
    Takes degrees converts to radians
    """
    return degrees*math.pi/180





