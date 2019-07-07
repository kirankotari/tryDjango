from django.http import HttpResponse
from django.shortcuts import render


def home_view(request, *args, **kwargs):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def content_view(request, *args, **kwargs):
    template = 'contact.html'
    context = {}
    return render(request, template, context)


def about_view(request, *args, **kwargs):
    template = 'about.html'
    context = {}
    return render(request, template, context)


def social_view(request, *args, **kwargs):
    return HttpResponse('<h1>Social Page</h1>')

