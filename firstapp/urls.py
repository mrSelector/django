from django.urls import path, re_path
from .views import hellodjango

urlpatterns = [
    re_path(r'^$', hellodjango)
    ]