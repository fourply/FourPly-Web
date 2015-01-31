from .models import UserProfile
from django.contrib.auth import authenticate


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
