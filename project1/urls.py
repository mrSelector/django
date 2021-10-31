from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^', include('firstapp.urls')),
    path('secondapp/', include('secondapp.urls')),
    path('thirdapp/', include('third_app.urls')),
    #path('fourthapp/', include('fourth_app.urls')),
    path('forms/', include('forms.urls')),
    path('' ,include('orm.urls'))

]