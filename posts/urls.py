from sys import path_hooks
from typing import Pattern
from django import urls
from django.urls import path 
from . import views#
from django.urls.resolvers import URLPattern#

urlpatterns = [
    path('', views.index, name ='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('likes/<int:post_id>/', views.likes, name='like'),
    path('edit/<int:post_id>/', views.edit, name='edit'),   
]