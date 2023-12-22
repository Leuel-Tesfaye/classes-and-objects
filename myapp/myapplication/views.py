from django.shortcuts import render
from django.http import HttpResponse
from .models import Features
# Create your views here.
def index(request):
    Feature = Features()
    Feature.id = 0
    Feature.name = 'Fast'
    Feature.details = 'Our services are faster than anyone else in the sector.'

    Feature2 = Features()
    Feature2.id = 1
    Feature2.name = 'Reliable'
    Feature2.details = 'Our services are more reliable than anyone else in the sector.'

    Feature3 = Features()
    Feature3.id = 2
    Feature3.name = 'Easy to use'
    Feature3.details = 'Our services are simpler than anyone else in the sector.'

    Feature4 = Features()
    Feature4.id = 3
    Feature4.name = 'Affordable'
    Feature4.details = 'Our services are more affordable than anyone else in the sector.'

    return render(request, 'index.html', {'Feature': Feature, 'Feature2': Feature2, 'Feature3': Feature3, 'Feature4': Feature4})


def counter(request):
    if 'text' in request.POST:
        text = request.POST['text']
        amount_of_words = len(text.split())
        return render(request, 'counter.html', {'amount': amount_of_words})
    else:
        pass 