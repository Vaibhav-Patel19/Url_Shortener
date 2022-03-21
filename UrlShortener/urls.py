
from os import name
from django.contrib import admin
from django.urls import path
from .views import index
from main import views

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('urls/', views.urlList, name = 'url-list'),
]
