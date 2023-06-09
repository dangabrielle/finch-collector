from django.shortcuts import render, redirect
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
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
    # First, create a list of the toy ids that the cat DOES have
    id_list = finch.toys.all().values_list('id', flat=True)
  # Now we can query for toys whose ids are not in the list using exclude
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()

    return render(request, 'finches/details.html', {'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have})


def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('details', finch_id=finch_id)


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


class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


def assoc_toy(request, finch_id, toy_id):
  # Note that you can pass a toy's id instead of the whole toy object
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)


def unassoc_toy(request, finch_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)
