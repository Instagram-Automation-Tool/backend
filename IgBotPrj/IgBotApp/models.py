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

#A lead is a connection to an account (established trough scraping or other outreach)
class Lead(models.Model):
    username = models.CharField(max_length=31, primary_key=True)
    foundBy = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    lastTimeUpdated = models.DateTimeField(auto_now=True)
    profileEverFetched = models.BooleanField(default=False)
    isFollower = models.BooleanField(default=False)
    isFollowed = models.BooleanField(default=False)
    isPrivate = models.BooleanField(default=True)
    isMessageable = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    bio=models.CharField(max_length=151, default="Bio not yet retrieved.")
    fullName = models.CharField(max_length=65, default="Name error!")
    profilePictureURL = models.CharField(max_length=10000, default="https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/281440578_1088265838702675_6233856337905829714_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent-ams2-1.cdninstagram.com&_nc_cat=1&_nc_ohc=WJLTPTMUm_AAX-gAuPW&edm=ABmJApABAAAA&ccb=7-5&oh=00_AfA1yOvK3rdFZQr7c5GvnRQpva1PKaKXW9FxC9LAI4VwqQ&oe=639E3F98&_nc_sid=6136e7")
    

    def __str__(self):
        return self.username



class Interaction(models.Model):
    reachedAccount = models.ForeignKey(Lead, on_delete=models.CASCADE)
    reachedWhileLoggedInAs = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)
    reachedAt = models.DateTimeField(auto_now_add=True)
    context = models.TextField(max_length=250)


    def __str__(self):
        return self.context
