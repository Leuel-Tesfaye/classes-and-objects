from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Features

def index(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')
def Login(request):
    # Your view logic here
    return render(request, 'login.html')
def counter(request):
    if 'text' in request.POST:
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    else:
        pass
