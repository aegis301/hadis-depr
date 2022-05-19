from django.forms import ModelForm
from .models import Item, NumericItem

class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'type', 'dataforms']
        

# class NumericItemCreationForm(ModelForm):
#     class Meta:
#         model = NumericItem
#         fields = ['title', 'description', 'type', 'dataforms']
        
        
    