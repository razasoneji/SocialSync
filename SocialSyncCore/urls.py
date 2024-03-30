from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # returning homepage of this folder
    # we are referring to the signup page
    path('signup', views.signup, name='signup'),
    # here we are referring to the settings page
    path('settings', views.settings, name='settings'),
    # here the media uploading page is concerned.
    path('upload', views.upload, name='upload'),
    # here the follow / unfollow thing is being updated.
    path('follow', views.follow, name='follow'),
    # here the searching of user is being concerned.
    path('search', views.search, name='search'),
    # here profile is being reffered.
    path('profile/<str:pk>', views.profile, name='profile'),
    # here the like/unlike is being addressed.
    path('like-post', views.like_post, name='like-post'),
    # this is a signinpage
    path('signin', views.signin, name='signin'),
    # this is a logot referring.
    path('logout', views.logout, name='logout'),
    # going to the about page
    path('about', views.about, name='about')
]
