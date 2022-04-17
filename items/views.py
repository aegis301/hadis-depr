from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
# Create your views here.
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "items/item_create.html"
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