from django.urls import path, include
from .views import index, index_render, index_redirect, red

urlpatterns = [
    path('', index),
    path('render/', index_render),
    path('redirect/', index_redirect),
    path('red/', red),

]

