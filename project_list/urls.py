from django.urls import path
from . import views

urlpatterns = [
    path('project_list', views.project_list)
]