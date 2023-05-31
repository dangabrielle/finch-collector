from django.shortcuts import render
from .models import Finch

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view


def cats_index(request):
    # We pass data to a template very much like we did in Express!
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })
