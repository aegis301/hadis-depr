from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
from dataforms.models import DataForm


def ItemCreateView(request, pk_df, *args, **kwargs):
    form = ItemForm()
    
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            df = DataForm.objects.filter(id=pk_df).first()
            return redirect(df)
            
    context = {'form': form}
    return render(request, "items/item_create.html", context)


def ItemUpdateView(request, pk_item, pk_df, *args, **kwargs):
    item = Item.objects.get(id=pk_item)
    form = ItemForm(instance=item)
    
    if request.method == 'POST':
        # print("Printing POST: ", request.POST, int(request.POST['dataforms']))
        form = ItemForm(request.POST, instance=item)
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