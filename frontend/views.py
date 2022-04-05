import os
from pyexpat import model

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from api.models import Patient, DataForm, Item, NumericItem, TextItem
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm


def home(request):
    return render(request, "frontend/home.html")


def forms(request):
    context = {"title": "Forms"}
    return render(request, "frontend/forms.html")


############################################################ Patient CRUD #####################################################


class PatientListView(LoginRequiredMixin, ListView):
    # automatically hands all retrieved objects down to the template as object_list
    model = Patient
    template_name = "frontend/patient_list.html"  # <app>/<model>_<viewtype>.html
    # context_object_name = 'patient'
    ordering = ["-created_at"]
    paginate_by = 12


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "frontend/patient_detail.html"


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "frontend/patient_create.html"
    fields = ["last_name", "first_name", "date_of_birth", "gender", "kis_id", "main_diagnosis"]

    # make custom form version to define required and non required fields
    def get_form(self, form_class=None):
        form = super(PatientCreateView, self).get_form(form_class)
        form.fields['main_diagnosis'].required = False
        return form
    # over write the default validation function
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    template_name = "frontend/patient_create.html"
    fields = ["last_name", "first_name", "date_of_birth", "gender", "kis_id", "main_diagnosis"]
    
    
    def get_form(self, form_class=None):
        form = super(PatientUpdateView, self).get_form(form_class)
        form.fields['main_diagnosis'].required = False
        return form
    # over write the default validation function
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    # custom test for user permission (used for UserPassesTestMixin)
    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.created_by:
            return True
        return False
    
class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Patient
    template_name = "frontend/patient_confirm_delete.html"
    success_url = "/patient/list/"

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.created_by:
            return True
        return False
    
class UserPatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "frontend/user_patient_list.html"  # <app>/<model>_<viewtype>.html
    context_object_name = 'patient'
    paginate_by = 12
    
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Patient.objects.filter(author=user).order_by('-created_at')
############################################################ DataForm and Item CRUD #####################################################    
class DataFormListView(LoginRequiredMixin, ListView):
    template_name = "frontend/dataform_list.html"
    model = DataForm
    
class DataFormDetailView(LoginRequiredMixin, DetailView):
    model = DataForm
    template_name = "frontend/dataform_detail.html"
    
# class DataFormUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = DataForm
#     template_name = "frontend/dataform_create.html"
#     fields = ["last_name", "first_name", "date_of_birth", "gender", "kis_id", "main_diagnosis"]
    
    
#     def get_form(self, form_class=None):
#         form = super(PatientUpdateView, self).get_form(form_class)
#         form.fields['main_diagnosis'].required = False
#         return form
#     # over write the default validation function
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#     # custom test for user permission (used for UserPassesTestMixin)
#     def test_func(self):
#         patient = self.get_object()
#         if self.request.user == patient.created_by:
#             return True
#         return False
    
class DataFormDeleteView(LoginRequiredMixin, DeleteView):
    model = DataForm
    template_name = "frontend/dataform_confirm_delete.html"
    success_url = "/dataform/list/"
############################################################ USER Management ############################################################
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
            messages.success(request, f"Your account has been updated!")
            return redirect("user-profile")

    else:  # its a get request, don't send any data, just display the forms
        u_update_form = UserUpdateForm(instance=request.user)
        p_update_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_update_form": u_update_form, "p_update_form": p_update_form}
    return render(request, "frontend/user_profile.html", context)
