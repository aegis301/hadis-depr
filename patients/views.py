from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from patients.models import Patient


############################################################ Patient CRUD #####################################################


class PatientListView(ListView):
    # automatically hands all retrieved objects down to the template as object_list
    model = Patient
    template_name = "patients/patient_list.html"  # <app>/<model>_<viewtype>.html
    # context_object_name = 'patient'
    ordering = ["-created_at"]
    paginate_by = 12


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patients/patient_detail.html"


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = "patients/patient_create.html"
    fields = [
        "last_name",
        "first_name",
        "date_of_birth",
        "gender",
        "kis_id",
        "main_diagnosis",
    ]

    # make custom form version to define required and non required fields
    def get_form(self, form_class=None):
        form = super(PatientCreateView, self).get_form(form_class)
        form.fields["main_diagnosis"].required = False
        return form

    # over write the default validation function
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    template_name = "patients/patient_create.html"
    fields = [
        "last_name",
        "first_name",
        "date_of_birth",
        "gender",
        "kis_id",
        "main_diagnosis",
    ]

    def get_form(self, form_class=None):
        form = super(PatientUpdateView, self).get_form(form_class)
        form.fields["main_diagnosis"].required = False
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
    template_name = "patients/patient_confirm_delete.html"
    success_url = "/patient/list/"

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.created_by:
            return True
        return False


