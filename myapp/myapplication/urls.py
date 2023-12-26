from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # When the path is empty (''), it represents the root URL
    path('counter/', views.counter, name='counter'),  
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'),  
    # path('logout/', views.logout, name='logout') 
]
