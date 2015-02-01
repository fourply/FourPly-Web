from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'health.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^api/v1/upload_photo', views.upload_photo,name="upload_photo"),
    url(r'^api/v1/new_user', views.new_user, name="new_user"),
    # url(r'^api/v1/add_review', views.add_review,name="add_review"),
    url(r'^api/v1/new_bathroom', views.new_bathroom,name="new_bathroom"),
    url(r'^api/v1/check_in', views.check_in,name="check_in"),
    url(r'^api/v1/add_rating', views.add_rating,name="add_rating"),
    url(r'^api/v1/heart_bathroom', views.heart_bathroom,name="heart_bathroom"),
    url(r'^api/v1/like_review', views.like_review,name="like_review"),
    url(r'^api/v1/get_nearby_bathrooms', views.get_nearby_bathrooms,name="get_nearby_bathrooms"),
    )