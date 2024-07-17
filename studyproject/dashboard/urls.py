from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('rooms', views.room,name="rooms"),
    path('calender', views.calender,name="calender"),
    path('progress', views.progress,name="progress"),
    path('quiz', views.quiz,name="quiz"),
    path('search', views.search,name="search"),
    path('resources', views.resources,name="resources")
    
]