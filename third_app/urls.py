from django.urls import path, include
from .views import index, nsx, civic
urlpatterns = [
    path('', index, name='Honda'),
    path('nsx/', nsx, name='NSX'),
    path('civic/', civic, name='civic'),
]