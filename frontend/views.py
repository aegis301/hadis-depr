import os
from pyexpat import model

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import MetaData, Table, create_engine, insert, select
from sqlalchemy.engine.base import Connection
from api.models import Patient

from api.models import Profile
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# custom env variable handling
load_dotenv(find_dotenv())
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PWD = os.getenv("POSTGRES_PWD")


def home(request):
    return render(request, "frontend/home.html")


def forms(request):
    context = {"title": "Forms"}
    return render(request, "frontend/forms.html")


class PatientListView(ListView):
    # automatically hands all retrieved objects down to the template as object_list
    model = Patient
    template_name = 'frontend/patient_list.html' # <app>/<model>_<viewtype>.html
    # context_object_name = 'patients'
    ordering = ['id']
    
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'frontend/patient_detail.html'
    
class PatientCreateView(CreateView):
    model = Patient
    template_name = 'frontend/patient_create.html'

def show_page(request):
    engine = create_engine(
        "postgresql://{}:{}@localhost:5432/hadis".format(POSTGRES_USER, POSTGRES_PWD)
    )

    conn: Connection
    with engine.connect() as conn:
        with conn.begin():
            meta = MetaData(conn)
            table = Table("api_patient", meta, autoload=True)
            stmt = select(table)
            patients = conn.execute(stmt)
            print(patients)

    context = {"patients": patients, "title": "List Patients"}
    return render(request, "frontend/patient_list.html", context)


# user registration form
def register_user(request):
    # if post request, send data
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Your accouunt has been created successfully! You are now able to log in.",
            )
            return redirect("user-login")
    else:
        # else its a get request, so just create an empty form
        form = UserRegistrationForm()
    return render(request, "frontend/user_registration.html", {"form": form})


@login_required
def user_profile(request):
    # is POST request, send data given along
    if request.method == "POST":
        u_update_form = UserUpdateForm(request.POST, instance=request.user)
        p_update_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_update_form.is_valid() and p_update_form.is_valid():
            u_update_form.save()
            p_update_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user-profile')

    else:  # its a get request, don't send any data, just display the forms
        u_update_form = UserUpdateForm(instance=request.user)
        p_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_update_form": u_update_form, "p_update_form": p_update_form}
    return render(request, "frontend/user_profile.html", context)
