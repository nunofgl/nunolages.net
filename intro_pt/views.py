#coding=utf-8

from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseRedirect


def homepage_pt(request):
    return render(request, 'homepage_pt.html')


def contact_pt(request):
    t = loader.get_template("contact_pt.html")
    return HttpResponse(t.render())


def thanks_pt(request):
    t = loader.get_template("thanks_pt.html")
    return HttpResponse(t.render())


def resubmit_pt(request):
    t = loader.get_template("resubmit_pt.html")
    return HttpResponse(t.render())


def biosketch_pt(request):
   t = loader.get_template("biosketch_pt.html")
   return HttpResponse(t.render())


def portfolio_pt(request):
    t = loader.get_template("portfolio_pt.html")
    return HttpResponse(t.render())


def links_pt(request):
    t = loader.get_template("links_pt.html")
    return HttpResponse(t.render())
