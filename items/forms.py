from django.forms import ModelForm
from .models import Item

class ItemCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'type', 'dataforms']
        


        
    