from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello HttpResponse</h1>")


def index_render(request):
    return render(request, 'index.html')


def index_redirect(request):
    return redirect('/secondapp/red')


def red(request):
    return HttpResponse('Hello redirect')
