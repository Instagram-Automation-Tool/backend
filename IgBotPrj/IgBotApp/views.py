from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import WebDriverManager


def PanelView(request):
    return render(request, "panel/panel.html")


def requestStoreCredentials(request):
    WebDriverManager.WebdriverActions.StoreLoginCredentials()
    return HttpResponse("Stored credentials")


def requestLoadCredentials(request):
    WebDriverManager.WebdriverActions.LoadSession()
    return HttpResponse("Loaded credentials")


def requestFollowProfile(request):
    WebDriverManager.WebdriverActions.FollowProfile(request.GET.get("username", ""))
    return HttpResponse("Followed guy")


def requestLikePost(request):
    WebDriverManager.WebdriverActions.LikePost(request.GET.get("link", ""))
    return HttpResponse("Liked post")


def requestCommentOnPost(request):
    WebDriverManager.WebdriverActions.CommentOnPost(
        request.GET.get("link", ""), request.GET.get("comment", "")
    )
    return HttpResponse("Commented")
