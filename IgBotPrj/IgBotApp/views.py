from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import botActions


def PanelView(request):
    template = loader.get_template("panel.html")
    return HttpResponse(template.render())


def requestStoreCredentials(request):
    botActions.WebdriverActions.StoreLoginCredentials()
    return HttpResponse("awdwa")
