from django.shortcuts import render, redirect
from .forms import ItemCreationForm, ItemInstanceCreationForm
from .models import Item
from dataforms.models import DataForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemListView(LoginRequiredMixin, ListView):
    # automatically hands all retrieved objects down to the template as object_list
    model = Item
    template_name = "items/item_list.html"  # <app>/<model>_<viewtype>.html
    ordering = ["-created_at"]
    # paginate_by = 12

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "items/item_detail.html"
    pk_url_kwarg = "pk_item"

def ItemCreateView(request, pk_df, *args, **kwargs):
    form = ItemCreationForm()
    
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
            df = DataForm.objects.filter(id=pk_df).first()
            return redirect(df)
            
    context = {'form': form}
    return render(request, "items/item_create.html", context)

def ItemInstanceCreateView(request, pk_df, *args, **kwargs):
    form = ItemInstanceCreationForm()
    
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemInstanceCreationForm(request.POST)
        if form.is_valid():
            form.save()
            df = DataForm.objects.filter(id=pk_df).first()
            return redirect(df)
            
    context = {'form': form}
    return render(request, "items/item_create.html", context)

def ItemUpdateView(request, pk_item, pk_df, *args, **kwargs):
    item = Item.objects.get(id=pk_item)
    form = ItemCreationForm(instance=item)
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemCreationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            df = DataForm.objects.filter(id=pk_df).first()
            return redirect(df)
        
            
    context = {'form': form}
    return render(request, "items/item_create.html", context)


def ItemDeleteView(request, pk_item, pk_df, *args, **kwargs):
    item = Item.objects.get(id=pk_item)
    if request.method == 'POST':
        df = DataForm.objects.filter(id=pk_df).first()
        item.delete()
        return redirect(df)
    context = {'object': item}
    
    return render(request, "items/item_confirm_delete.html", context)