from django.db import models
from django.urls import reverse
from django.utils import timezone
from model_utils.managers import InheritanceManager # improve querying in inheritance models
from dataforms.models import DataForm
from patients.models import Patient

# Create your models here.
class Item(models.Model):
    NUMERIC = "NUM"
    TEXT = "TEXT"
    BOOLEAN = "BOOL"
    DATE = "DATE"
    
    objects = InheritanceManager()

    name = models.CharField(max_length=200)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    
    DataForm = models.ForeignKey(DataForm, on_delete=models.CASCADE)
    patients = models.ManyToManyField(Patient)
    
    ITEM_TYPE_CHOICES = (
        (NUMERIC, "Numeric value"), 
        (TEXT, "Text or Characters"),
        (BOOLEAN, "Yes or No"),
        (DATE, "Date and Time")
        )
    type = models.TextField(
        choices=ITEM_TYPE_CHOICES
    )
    
    def get_absolute_url(self):
        return reverse("dataform-detail", kwargs={"pk": self.pk})
    
class NumericItem(Item):
    value = models.FloatField(blank=True, null=True)
    type = "NUM"
    def __str__(self) -> str:
        return self.name
    
class TextItem(Item):
    value = models.TextField(blank=True, default="")
    type = "TEXT"
    def __str__(self) -> str:
        return self.name
    
class BooleanItem(Item):
    value = models.BooleanField(blank=True, null=True)
    type = "BOOL"
    def __str__(self) -> str:
        return self.name
    
class DateItem(Item):
    value = models.DateTimeField(blank=True, null=True)
    type = "DATE"
    def __str__(self) -> str:
        return self.name
    
### categorical items
### range items