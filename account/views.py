from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# @login_required
# def index(request):
#     return render(request, 'base.html', {'section': 'index'})