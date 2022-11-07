from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class InstagramAccount(models.Model):
    expandiId = models.CharField(max_length=100)
    username = models.CharField(max_length=31, primary_key=True)
    password = models.CharField(max_length=120)
    cookies = models.JSONField()
    proxy = models.CharField(max_length=100)

    def __str__(self):
        return self.username
