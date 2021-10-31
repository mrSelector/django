from django.contrib import admin
from django.urls import path, re_path
from .views import IndexTemplate
urlpatterns = [
    path('', IndexTemplate.as_view())
]