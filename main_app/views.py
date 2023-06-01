from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view


def finch_index(request):
    # We pass data to a template very much like we did in Express!
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })


def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/details.html', {'finch': finch})


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']
    # success_url = '/cats/' not the preferred way. refer to models


class FinchUpdate(UpdateView):
    model = Finch
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'age']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
