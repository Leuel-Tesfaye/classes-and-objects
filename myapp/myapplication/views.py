from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render  # Add import for render
from .models import Features

def index(request):
    features = Features.objects.all()  # Rename variable to lowercase 'features'
    return render(request, 'index.html', {'features': features})  # Adjust variable name in the context dictionary

def register (request) : 
    return render(request, 'register.html')

def counter(request):
    if 'text' in request.POST:
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    else:
        pass

