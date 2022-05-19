from django.forms import ModelForm
from .models import Item, NumericItem

class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'type', 'dataforms']
        

class ItemInstanceCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = []
        
        
    