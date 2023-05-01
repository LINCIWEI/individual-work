from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('chart/', views.country_chart,name='chart')

]
