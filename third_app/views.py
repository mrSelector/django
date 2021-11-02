from django.shortcuts import render


def index(request):
    return render(request, 'base.html')


def nsx(request):
    return render(request, 'nsx.html')


def civic(request):
    return render(request, 'civic.html')

