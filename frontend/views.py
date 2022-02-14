import os

from django.contrib import messages
from django.shortcuts import redirect, render
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import MetaData, Table, create_engine, insert, select
from sqlalchemy.engine.base import Connection
from .forms import UserRegistrationForm

# custom env variable handling
load_dotenv(find_dotenv())
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PWD = os.getenv('POSTGRES_PWD')


def home(request):
    return render(request, 'frontend/home.html')


def forms(request):
    context = {
        'title': 'Forms'
    }
    return render(request, 'frontend/forms.html')


def show_page(request):
    engine = create_engine(
        'postgresql://{}:{}@localhost:5432/hadis'.format(POSTGRES_USER, POSTGRES_PWD))

    conn: Connection
    with engine.connect() as conn:
        with conn.begin():
            meta = MetaData(conn)
            table = Table('api_patient', meta, autoload=True)
            stmt = select(table)
            patients = conn.execute(stmt)
            print(patients)

    context = {
        'patients': patients,
        'title': 'Show Patients'
    }
    return render(request, 'frontend/show_page.html', context)


# user registration form
def register_user(request):
    # if post request, send data
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('hadis-home')
    else:
        # else its a get request, so just create an empty form
        form = UserRegistrationForm()
    return render(request, 'frontend/user_registration.html', {
        'form': form
    })


def login_user(request):
    return render(request, 'frontend/user_login.html')
