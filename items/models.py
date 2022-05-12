from turtle import Turtle
from django.db import models
from django.urls import reverse
from django.utils import timezone
from model_utils.managers import InheritanceManager # improve querying in inheritance models


# Create your models here.
class Item(models.Model):
    NUMERIC = "NUM"
    TEXT = "TEXT"
    
    objects = InheritanceManager()

    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    recorded_at = models.DateTimeField(blank=True, null=True)
    
    dataforms = models.ManyToManyField(to="dataforms.DataForm", blank=True)
    visits = models.ManyToManyField(to="patients.Visit", blank=True)
  
    ITEM_TYPE_CHOICES = (
        (NUMERIC, "Numeric value"), 
        (TEXT, "Text or Characters")
        )
    type = models.TextField(
        choices=ITEM_TYPE_CHOICES
    )
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("dataform-detail", kwargs={"pk": self.pk})
    
class NumericItem(Item):
    value = models.FloatField(blank=True, null=True)
    type = "NUM"
        
class TextItem(Item):
    value = models.TextField(blank=True, default="")
    type = "TEXT"
    
# class BooleanItem(models.Model):
#     value = models.BooleanField(blank=True, null=True)
#     type = "BOOL"
#     def __str__(self) -> str:
#         return self.name
    
# class DateItem(models.Model):
#     value = models.DateTimeField(blank=True, null=True)
#     type = "DATE"
#     def __str__(self) -> str:
#         return self.name
    
### categorical items
### range items