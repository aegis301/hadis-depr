from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from patients.models import Patient

from .forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm


# Create your views here.
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
    return render(request, "users/user_registration.html", {"form": form})


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
    return render(request, "users/user_profile.html", context)


class UserPatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "users/user_patient_list.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "patient"
    paginate_by = 12

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Patient.objects.filter(author=user).order_by("-created_at")
