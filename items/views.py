from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
from dataforms.models import DataForm


def ItemCreateView(request, *args, **kwargs):
    form = ItemForm()
    
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # safe the dataform id
            if type(request.POST['dataforms']) is list:
                df_id = request.POST['dataforms'][0]
            else:
                df_id = request.POST['dataforms']
                
            redirect('dataform-detail', pk=df_id)
    context = {'form': form}
    return render(request, "items/item_create.html", context)


def ItemUpdateView(request, pk_item, *args, **kwargs):
    
    item = Item.objects.get(id=pk_item)
    form = ItemForm(instance=item)
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # safe the dataform id
            if type(request.POST['dataforms']) is list:
                df_id = request.POST['dataforms'][0]
            else:
                df_id = request.POST['dataforms']
                
            redirect('dataform-detail', pk=df_id)
    context = {'form': form}
    return render(request, "items/item_create.html", context)


def ItemDeleteView(request, *args, **kwargs):
    
    context = {}
    
    return render(request, "items/item_confirm_delete.html", context)