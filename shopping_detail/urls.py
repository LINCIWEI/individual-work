from django.urls import path
from . import views

urlpatterns = [
    path('<str:detail_id>/', views.shopping_detail, name='shopping_detail'),
]