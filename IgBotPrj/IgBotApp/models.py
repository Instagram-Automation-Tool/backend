from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# add bio
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


class Follower(models.Model):
    fullName = models.CharField(max_length=65)
    isVerified = models.BooleanField()
    profilePictureURL = models.URLField()

    def ParseJSON(self, json):
        self.fullName = json
