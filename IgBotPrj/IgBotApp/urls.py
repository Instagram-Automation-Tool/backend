from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.PanelView, name="panel_view"),
    path(
        "storecredentials",
        views.requestStoreCredentials,
        name="function_storecredentials",
    ),
]
