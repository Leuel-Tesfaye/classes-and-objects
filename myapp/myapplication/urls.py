from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # When the path is empty (''), it represents the root URL
    path('counter', views.counter, name= 'counter')
]
