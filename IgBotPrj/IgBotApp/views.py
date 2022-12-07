from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from . import WebDriverManager
from IgBotApp.models import InstagramAccount
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status

# todo: improve request responses and actually process inputs
def requestStoreCredentials(request):
    WebDriverManager.WebdriverActions.StoreLoginCredentials(
        request.GET.get("username"), request.GET.get("password")
    )
    return HttpResponse("Stored credentials")


def requestLoadCredentials(request):
    WebDriverManager.WebdriverActions.LoadSession(request.GET.get("username"))
    return HttpResponse("Loaded credentials")


def requestFollowProfile(request):
    WebDriverManager.WebdriverActions.FollowProfile(
        request.GET.get("link", ""), request.GET.get("username")
    )
    return HttpResponse("Followed guy")


def requestLikePost(request):
    WebDriverManager.WebdriverActions.LikePost(
        request.GET.get("link", "")
    , request.GET.get("username"))
    return HttpResponse("Liked post")


def requestCommentOnPost(request):
    WebDriverManager.WebdriverActions.CommentOnPost(
        request.GET.get("link"),
        request.GET.get("comment"),
        request.GET.get("username"),
    )
    return HttpResponse("Commented")

def requestCommentOnProfilePosts(request):
    comments = []
    comment=request.GET.get("comment")
    count=int(request.GET.get("count"))
    while(count>0):
        comments.append(comment)
        count=count-1
    return HttpResponse(
        WebDriverManager.WebdriverActions.CommentOnProfilePosts(
            request.GET.get("targetUsername"),
            comments,
            request.GET.get("like")=="on",
            request.GET.get("username")
        )
    )

def requestScrapeFollowers(request):
    return HttpResponse(
        WebDriverManager.WebdriverActions.ScrapeFollowers(
            request.GET.get("link"),
            request.GET.get("amount"),
            request.GET.get("username"),
        )
    )


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
        return Response(accounts, status= status.HTTP_200_OK)
