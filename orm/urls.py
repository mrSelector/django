from django.contrib import admin
from django.urls import path, re_path
from .views import IndexTemplate, delete_record
urlpatterns = [
    path('', IndexTemplate.as_view()),
    re_path(r'^([\d]{1})$', delete_record)
]