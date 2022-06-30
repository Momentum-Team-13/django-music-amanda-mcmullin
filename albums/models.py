from django.db import models
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    artist = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    