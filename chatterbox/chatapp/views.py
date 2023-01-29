from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import AppUser


def chatter(request):
    myusers = AppUser.objects.all()
    context: {
        'myusers': myusers,
    }
    return render(request,'chatter.html', {'myusers': myusers })

def details(request,id):
    myusers = AppUser.objects.get(id=id)
    context: {
        'myusers': myusers,
    }
    return render(request,'details.html', {'myusers': myusers })
