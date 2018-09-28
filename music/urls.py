from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('musicview/<name>/',views.music_view1,name='one'),
]