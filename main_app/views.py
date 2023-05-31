from django.shortcuts import render

# Create your views here.
finches = [
    {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
    {'name': 'Sachi', 'breed': 'calico',
        'description': 'gentle and loving', 'age': 2},
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# Add new view


def cats_index(request):
    # We pass data to a template very much like we did in Express!
    return render(request, 'finches/index.html', {
        'finches': finches
    })
