from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('readingview/<name>/',views.reading_view1,{'switch':'true'})
]
