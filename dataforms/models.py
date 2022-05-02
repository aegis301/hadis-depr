from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class DataForm(models.Model):
    
    ### establish a many to many relationship with the Patients!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    title = models.CharField(max_length=200)
    description = models.TextField(default=None)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING
    )
    
    numeric_items = models.ManyToManyField(to='items.NumericItem')
    text_items = models.ManyToManyField(to='items.TextItem')
    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("dataform-detail", kwargs={"pk": self.pk})
    
