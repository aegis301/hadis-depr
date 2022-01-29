from django.shortcuts import render
from django.http import HttpResponse

patients = [
    {
        'first_name': 'Max',
        'last_name': 'Powers',
        'main_diagnosis': 'Awesomeritis',
        'date_of_birth': '01.01.1990'
    },
    {
        'first_name': 'Gandalf',
        'last_name': 'Gray',
        'main_diagnosis': 'Whiteness',
        'date_of_birth': '01.01.1800'
    }
]

# Create your views here.


def home(request):
    return render(request, 'frontend/home.html')


def forms(request):
    return render(request, 'frontend/forms.html')


def show_page(request):
    context = {
        'patients': patients,
        'title': 'Show Patients'
    }
    return render(request, 'frontend/show_page.html', context)
