from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.mail import send_mail


def homepage(request):
    return render(request, 'homepage.html')


def contact(request):
    t = loader.get_template("contact.html")
    return HttpResponse(t.render())


def thanks(request):
    t = loader.get_template("thanks.html")
    return HttpResponse(t.render())


def biosketch(request):
    t = loader.get_template("biosketch.html")
    return HttpResponse(t.render())


def portfolio(request):
    t = loader.get_template("portfolio.html")
    return HttpResponse(t.render())


def links(request):
    t = loader.get_template("links.html")
    return HttpResponse(t.render())
