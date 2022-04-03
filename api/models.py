from email.policy import default
# from djongo import models

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
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

    def __str__(self):
        return self.first_name + " " + self.last_name

    # how to redirect after create (reverse returs string representation of the full path, not actually redirect)
    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})


class Item(models.Model):
    NUMERIC = "NUM"
    TEXT = "TEXT"
    BOOLEAN = "BOOL"
    DATE = "DATE"

    name = models.CharField(max_length=200)
    description = models.TextField(default=None)
    ITEM_TYPE_CHOICES = (
        (NUMERIC, "Numeric value"), 
        (TEXT, "Text or Characters"),
        (BOOLEAN, "Yes or No"),
        (DATE, "Date and Time")
        )
    type = models.TextField(
        choices=ITEM_TYPE_CHOICES, default=TEXT
    )

class NumericItem(Item):
    value = models.FloatField()
    
class TextItem(Item):
    value = models.TextField()

class BooleanItem(Item):
    value = models.BooleanField()
    
class DateItem(Item):
    value = models.DateTimeField()

class DataForm(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    items = models.ManyToManyField(Item)

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title


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
