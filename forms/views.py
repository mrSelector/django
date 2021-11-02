from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .forms import HumanForm


def index(request:HttpRequest):
    form = HumanForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            form.save()
            return HttpResponse("Форма сохранена")
        return HttpResponse('ERROR')
    return render(request, 'body.html', {'form': form})


