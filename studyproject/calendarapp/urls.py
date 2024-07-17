# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar, name='calendar'),
    path('create_event/', views.create_event, name='create_event'),
]
