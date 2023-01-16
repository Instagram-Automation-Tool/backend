from django.contrib import admin
from django.urls import path, include, re_path
from .views import AccountsRetrieveUpdateAPIView, InteractionsRetrieveAPIView
from . import views

urlpatterns = [
    path("", views.PanelView, name="panel_view"),
    path(
        "storeCredentials",
        views.requestStoreCredentials,
    ),
    path(
        "loadCredentials",
        views.requestLoadCredentials,
    ),
    path("notifications", views.requestFetchNotifications),
    path(
        "follow",
        views.requestFollowProfile,
    ),
    path("like", views.requestLikePost),
    path("comment", views.requestCommentOnPost),
    path("commentOnProfilePosts", views.requestCommentOnProfilePosts),
    path("followUsernames", views.requestFollowUsernames),
    path("likePostsOfUsernamesProfiles", views.requestLikePostsOfUsernamesProfiles),
    path("scrapeHashtag", views.requestScrapeHashtag),
    path("scrapeFollowers", views.requestScrapeFollowers),
    path("accounts", AccountsRetrieveUpdateAPIView.as_view(), name="user"),
    path("interactions", InteractionsRetrieveAPIView.as_view(), name="interactions"),
]
