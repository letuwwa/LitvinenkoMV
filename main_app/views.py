from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request, 'base.html', context={})


def contacts(request):
    return render(request, 'other/contacts.html', context={})
