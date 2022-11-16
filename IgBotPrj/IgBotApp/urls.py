from django.contrib import admin
from django.urls import path, include, re_path
from .views import (
    AccountsRetrieveUpdateAPIView,
)
from . import views

urlpatterns = [
    path("", views.PanelView, name="panel_view"),
    path(
        "storecredentials",
        views.requestStoreCredentials,
    ),
    path(
        "loadcredentials",
        views.requestLoadCredentials,
    ),
    path(
        "follow",
        views.requestFollowProfile,
    ),
    path("like", views.requestLikePost),
    path("comment", views.requestCommentOnPost),
    path("commentOnProfilePosts", views.requestCommentOnProfilePosts),
    path("scrapefollowers", views.requestScrapeFollowers),
    path('accounts', AccountsRetrieveUpdateAPIView.as_view(), name='user'),

]
