from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('upload/', views.upload_resource, name='upload_resource'),
    path('download/<int:resource_id>/', views.download_resource, name='download_resource'),
]
