from django.urls import path
from .views import login_sau

urlpatterns = [
    #path('register', RegisterView.as_view()),
    path('login', login_sau, name="Login"),
]
