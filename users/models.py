from email.policy import default
from tkinter import NUMERIC
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from model_utils.managers import InheritanceManager # improve querying in inheritance models
from PIL import Image


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