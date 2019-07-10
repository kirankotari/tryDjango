from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm
# from django.contrib.auth.views import
# from django.contrib.auth.urls import


def home_view(request, *args, **kwargs):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def content_view(request, *args, **kwargs):
    template = 'contact.html'
    title = 'Contact'
    cofirm_message = None
    form = contactForm(request.POST or None)
    if form.is_valid():
        print(request.POST)
        message = '{} {}'.format(form.cleaned_data['name'], form.cleaned_data['comment'])
        send_mail(
            'Subject Sample Message',
            message,
            form.cleaned_data['email'],
            [settings.EMAIL_HOST_USER],
            fail_silently=True)
        title = "Thanks!"
        cofirm_message = "Thanks for the message. We will get right back to you."
        form = None

    context = {'title': title, 'cofirm_message': cofirm_message, 'form': form}
    return render(request, template, context)


def about_view(request, *args, **kwargs):
    template = 'about.html'
    context = {}
    return render(request, template, context)


def social_view(request, *args, **kwargs):
    return HttpResponse('<h1>Social Page</h1>')


@login_required
def userProfile(request, *args, **kwargs):
    template = 'dashboard.html'
    context = {'user': request.user}
    return render(request, template, context)

