from django.urls import path, re_path
from .views import IndexView, RegisterView, LoginView, LogoutView
urlpatterns = [
    path('', IndexView.as_view(),name='home'),
    path('register',RegisterView.as_view(),name='register'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
]