from django.shortcuts import render
from django.http import HttpResponse

patients = [
    {
        'id': '12345',
        'first_name': 'Legolas',
        'last_name': 'Grunblatt',
        'main_diagnosis': 'Awesomeritis',
        'date_of_birth': '01.01.1990'
    },
    {
        'id': '67899',
        'first_name': 'Gandalf',
        'last_name': 'Gray',
        'main_diagnosis': 'Whiteness',
        'date_of_birth': '01.01.1800'
    },
    {
        'id': '67289',
        'first_name': 'Gimli',
        'last_name': 'Gloinsson',
        'main_diagnosis': 'Stubbornness',
        'date_of_birth': '01.01.1970'
    },
    {
        'id': '25942',
        'first_name': 'Aragorn',
        'last_name': 'Streicher',
        'main_diagnosis': 'Kingliness',
        'date_of_birth': '01.01.1975'
    }
]

# Create your views here.


def home(request):
    return render(request, 'frontend/home.html')


def forms(request):
    context = {
        'title': 'Forms'
    }
    return render(request, 'frontend/forms.html')


def show_page(request):
    context = {
        'patients': patients,
        'title': 'Show Patients'
    }
    return render(request, 'frontend/show_page.html', context)
