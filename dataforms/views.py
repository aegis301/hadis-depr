from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import DataFormTemplate, Item


############################################################ DataFormTemplate CRUD #####################################################
class DataFormTemplateListView(LoginRequiredMixin, ListView):
    template_name = "dataforms/dataform_list.html"
    model = DataFormTemplate


class DataFormTemplateDetailView(LoginRequiredMixin, DetailView):
    model = DataFormTemplate
    template_name = "dataforms/dataform_detail.html"


class DataFormTemplateCreateView(LoginRequiredMixin, CreateView):
    model = DataFormTemplate
    template_name = "dataforms/dataform_create.html"
    fields = ["title", "description"]

    # make custom form version to define required and non required fields
    def get_form(self, form_class=None):
        form = super(DataFormTemplateCreateView, self).get_form(form_class)
        return form

    # over write the default validation function
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class DataFormTemplateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DataFormTemplate
    template_name = "dataforms/dataform_create.html"
    fields = ["title", "description"]

    def get_form(self, form_class=None):
        form = super(DataFormTemplateUpdateView, self).get_form(form_class)
        return form

    # over write the default validation function
    def form_valid(self, form):
        return super().form_valid(form)

    # custom test for user permission (used for UserPassesTestMixin)
    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.created_by:
            return True
        return False


class DataFormTemplateDeleteView(LoginRequiredMixin, DeleteView):
    model = DataFormTemplate
    template_name = "dataforms/dataform_confirm_delete.html"
    success_url = "/dataform/list/"


############################################################ DataFormTemplate CRUD #####################################################
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "dataforms/item_create.html"
    fields = ["name", "description", "type"]
    # make custom form version to define required and non required fields
    def get_form(self, form_class=None):
        form = super(ItemCreateView, self).get_form(form_class)
        # form.fields['main_diagnosis'].required = False
        return form

    # over write the default validation function
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
