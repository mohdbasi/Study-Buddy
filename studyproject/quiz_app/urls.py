# quiz_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('osquiz', views.osquiz, name = 'osquiz'),
    path('coaquiz', views.coaquiz, name = 'coaquiz'),
    path('oopquiz', views.oopquiz, name = 'oopquiz')
]
