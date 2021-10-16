from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('blog/show/', views.show, name='index')
]