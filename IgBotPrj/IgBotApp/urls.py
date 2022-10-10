from django.contrib import admin
from django.urls import path, include, re_path

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
        "follow/<username>",
        views.requestFollowProfile,
    ),
    re_path("like", views.requestLikePost),
]
