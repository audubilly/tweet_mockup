from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_tweet, name='new_tweet'),


]
