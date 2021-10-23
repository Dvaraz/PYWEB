from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'blog'

urlpatterns = [
    path('blog/show/', views.BlogShow.as_view(), name='blog_list'),
    path('blog/showgen/', views.BlogShowGeneric.as_view(), name='blog_list_gen'),
    path('blog/about/', views.blog_version, name='version')
]