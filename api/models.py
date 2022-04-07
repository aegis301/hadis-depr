from email.policy import default
from tkinter import NUMERIC
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
    
    
class Patient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    kis_id = models.CharField(max_length=8)
    gender = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,  # don't delete patients if a user is deleted
        # default=User.objects.filter(username='christian')
    )
    main_diagnosis = models.CharField(max_length=1000, blank=False)
    dataforms = models.ManyToManyField(DataFormTemplate)

    def __str__(self):
        return self.first_name + " " + self.last_name

    # how to redirect after create (reverse returs string representation of the full path, not actually redirect)
    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        # get image path and open it
        img = Image.open(self.image.path)

        # if too big, resize and overwrite image with output
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
