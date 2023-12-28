# urls.py in the 'register' app
from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.index, name='index'),
    path('counter/', views.counter, name='counter'),  # Use / at the end for consistency
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]
