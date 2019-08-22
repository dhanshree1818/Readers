from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from reader_app import forms
# Create your views here.
from reader_app.forms import RegisterForm


def index(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})