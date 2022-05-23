from django.forms import ModelForm
from items.models import Item, NumericItem
from dataforms.models import DataForm

class ItemInstanceCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = []
        
class DataformAddValues(ModelForm):
    class Meta:
        model = DataForm
        fields= []