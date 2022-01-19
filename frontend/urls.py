from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="list"),
    path('table/', views.tablesjoin, name="table")

]
