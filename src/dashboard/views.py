from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request, *args, **kwargs):
    template = 'dashboard.html'
    context = {}
    return render(request, template, context)
