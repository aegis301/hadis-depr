from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from model_utils.managers import InheritanceManager # improve querying in inheritance models
from PIL import Image
# Create your models here.


class Item(models.Model):
    NUMERIC = "NUM"
    TEXT = "TEXT"
    BOOLEAN = "BOOL"
    DATE = "DATE"
    
    objects = InheritanceManager()

    name = models.CharField(max_length=200)
    description = models.TextField(default=None)
    ITEM_TYPE_CHOICES = (
        (NUMERIC, "Numeric value"), 
        (TEXT, "Text or Characters"),
        (BOOLEAN, "Yes or No"),
        (DATE, "Date and Time")
        )
    type = models.TextField(
        choices=ITEM_TYPE_CHOICES
    )
    value = models.JSONField()
    def get_absolute_url(self):
        return reverse("dataform-detail", kwargs={"pk": self.pk})

# class NumericItem(Item):
#     value = models.FloatField(blank=True, null=True)
#     type = "NUM"
#     def __str__(self) -> str:
#         return self.name
# class TextItem(Item):
#     value = models.TextField(blank=True, default="")
#     type = "TEXT"
#     def __str__(self) -> str:
#         return self.name
# class BooleanItem(Item):
#     value = models.BooleanField(blank=True, null=True)
#     type = "BOOL"
#     def __str__(self) -> str:
#         return self.name
# class DateItem(Item):
#     value = models.DateTimeField(blank=True, null=True)
#     type = "DATE"
#     def __str__(self) -> str:
#         return self.name
    
### categorical items
### range items

class DataFormTemplate(models.Model):
    
    ### establish a many to many relationship with the Patients!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    items = models.ManyToManyField(Item, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("dataform-detail", kwargs={"pk": self.pk})
    