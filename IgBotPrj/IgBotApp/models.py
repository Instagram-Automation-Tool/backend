from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class InstagramAccount(models.Model):
    expandiId = models.CharField(max_length=100)
    username = models.CharField(max_length=31)
    cookies = models.TextField()
    proxy = models.CharField(max_length=100)
