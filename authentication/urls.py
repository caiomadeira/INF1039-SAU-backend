from django.urls import path
from .views import RegisterView, LoginView
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
]
