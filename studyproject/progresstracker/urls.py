# progress/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:task_id>/', views.progress_details, name='progress_details'),
    path('progress/<int:task_id>/update/', views.update_progress, name='update_progress'),
]
