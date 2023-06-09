from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import AppUser


def chatter(request):
    myusers = AppUser.objects.all().values()
    context = {'myusers': myusers}
    return render(request, 'chatter.html', context)


def details(request, id):
    myusers = AppUser.objects.get(id=id)
    context = {'myusers': myusers}
    return render(request, 'details.html', context)


def main(request):
    return render(request, 'main.html')
