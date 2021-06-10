from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index),
    path('create',views.index2),
    path('success',views.index3),
    path('login',views.index4),
    path('logout',views.index5),
    path('Class IX Maths',views.index6),
     path('About Us',views.index7),
     
]