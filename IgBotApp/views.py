from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from . import WebDriverManager
from IgBotApp.models import InstagramAccount, Interaction
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
import json


# region API endpoints
def requestStoreCredentials(request):
    WebDriverManager.WebdriverActions.StoreLoginCredentials(
        request.GET.get("username"), request.GET.get("password")
    )
    return HttpResponse("Stored credentials")


def requestLoadCredentials(request):
    WebDriverManager.WebdriverActions.LoadSession(request.GET.get("username"))
    return HttpResponse("Loaded credentials")


def requestFetchNotifications(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.FetchNotifications(
            request.GET.get("username")
        )
    )


def requestFollowProfile(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.FollowProfile(
            request.GET.get("link", ""), request.GET.get("username")
        )
    )


def requestLikePost(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.LikePost(
            request.GET.get("link", ""), request.GET.get("username")
        )
    )


def requestCommentOnPost(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.CommentOnPost(
            request.GET.get("link"),
            request.GET.get("comment"),
            request.GET.get("username"),
        )
    )


def requestCommentOnProfilePosts(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.CommentOnProfilePosts(
            request.GET.get("targetUsername"),
            request.GET.get("comments").split(","),
            request.GET.get("like") == "on",
            request.GET.get("username"),
        )
    )


def requestFollowUsernames(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.FollowUsernames(
            request.GET.get("targets").replace(" ", "").split(","),
            request.GET.get("username"),
        )
    )


def requestLikePostsOfUsernamesProfiles(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.LikePostsOfUsernamesProfiles(
            request.GET.get("targets").replace(" ", "").split(","),
            request.GET.get("count"),
            request.GET.get("username"),
        )
    )


def requestScrapeHashtag(request):
    args = {}
    args["username"] = "cold.stored.entertainment"
    return HttpResponse(
        json.dumps(
            WebDriverManager.WebdriverActions.ScrapeHashtag(
                request.GET.get("hashtag"),
                request.GET.get("username"),
                request.GET.get("noOfFollowersToScrape", 100),
                request.GET.get("noOfPostsToScrape", 10),
                request.GET.get("hashtagOption", 0),
            )
        )
    )


def requestScrapeFollowers(request):
    return HttpResponse(
        json.dumps(
            WebDriverManager.WebdriverActions.ScrapeFollowers(
                request.GET.get("link"),
                request.GET.get("amount"),
                request.GET.get("username"),
            )
        )
    )


# endregion


# region showcase panel
def PanelView(request):
    accounts = InstagramAccount.objects.all().values()
    if accounts == None:
        accounts = []
    return render(request, "panel/panel.html", {"accounts": accounts})


# endregion


# get all acounts
class AccountsRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    def retrieve(self, request):
        accounts = InstagramAccount.objects.all().values()
        return Response(accounts, status=status.HTTP_200_OK)


class InteractionsRetrieveAPIView(RetrieveUpdateAPIView):
    def retrieve(self, request):
        interactions = Interaction.objects.all().values()
        return Response(interactions, status=status.HTTP_200_OK)
