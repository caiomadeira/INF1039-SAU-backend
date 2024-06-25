from django.contrib import admin
from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

from authentication.views import login_sau, login_sucess

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/student/', include('student.urls')),
    path('', api_home, name='SAU Backend'),
    path('login', login_sau, name='Login test'),
    path('sucess', login_sucess, name='Login Sucess')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)