from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models


class InstagramAccount(models.Model):
    expandiId = models.CharField(max_length=100)
    username = models.CharField(max_length=31, primary_key=True)
    password = models.CharField(max_length=120)
    cookies = models.JSONField()
    proxy = models.CharField(max_length=100)
    bio = models.CharField(max_length=151)
    followerCount = models.IntegerField()
    followingCount = models.IntegerField(default=-1)
    postsCount = models.IntegerField(default=-1)
    profilePictureURL = models.CharField(max_length=100000)

    def __str__(self):
        return self.username

class ExternalInstagramAccount(models.Model):

    username = models.CharField(max_length=31, primary_key=True)
    bio=models.CharField(max_length=151)
    fullName = models.CharField(max_length=65)
    isVerified = models.BooleanField()
    profilePictureURL = models.URLField()
    
    def ParseJSON(self, json):
        self.fullName = json



class Interaction_HashtagScraped(models.Model):
    reachedAccount = models.ForeignKey(ExternalInstagramAccount, on_delete=models.CASCADE, primary_key=True)
    reachedWhileLoggedInAs = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    reachedAt = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.account.username

    class Meta:
        ordering = ['reachedAt']   
