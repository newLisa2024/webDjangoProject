from django.shortcuts import render


def index(request):
    data = {
        'caption': 'CatDjango'
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

# Create your views here.
