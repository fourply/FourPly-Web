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
    return values


def bad_request(error):
    response_data = {'error': error}
    return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)


def auth_failed():
    response_data = {'error': "authentication failed"}
    return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)