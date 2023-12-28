from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Features

def index(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login:login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register:register')  # Corrected indentation
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid !')
            return redirect('login:login')  # Corrected indentation
    else:
        return render(request, 'login.html')

def counter(request):
    if 'text' in request.POST:
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    else:
        pass
