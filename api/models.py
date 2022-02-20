from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    kis_id = models.CharField(max_length=12)
    gender = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    # created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING) # don't delete patients if a user is deleted
    main_diagnosis = models.CharField(max_length=1000, blank=False)
    
class DataForms(models.Model):
    name = models.CharField(max_length=200)
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    
    