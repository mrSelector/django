from django.http import HttpResponse


def hellodjango(request):
    return HttpResponse("Hello Django!")
