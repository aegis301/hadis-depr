from django.forms import ModelForm
from items.models import Item, NumericItem

class ItemInstanceCreationForm(ModelForm):
    class Meta:
        model = Item
        fields = []
        