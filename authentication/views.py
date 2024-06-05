from django.shortcuts import render, redirect
from rest_framework.generics import GenericAPIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from scrapper.login import *
from django.template import loader
from django.http import HttpResponse

from student.models import Student
from .forms import LoginStudentForm


# Herda de GenericApiView para poder lidar com qualquer tipo de request
class RegisterView(GenericAPIView):
    serializer_class = StudentSerializer
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#class LoginView(GenericAPIView):
    #serializer_class = StudentSerializer
    #def post(self, request):
        #data = request.data 
        #username = data.get('username', '')
        #password = data.get('password', '')
        #user = auth.authenticate(username=username, password=password)
        #if user:
            #auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)
            
            #serializer = StudentSerializer(user)
            #data = {'user': serializer.data, 'token': auth_token, "status_code": status.HTTP_200_OK, "status_msg": "usuario logado."}
            
            #return Response(data, status=status.HTTP_200_OK)
        
        #return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
def login_sau(request):
    form = LoginStudentForm(request.GET)
    if form.is_valid():
        user = form.cleaned_data['username']
        password = form.cleaned_data['password']
        username_sau = str(make_login(hide_browser=True, user=user, password=password))
        return render(request, 'login_sucess.html', {'username': username_sau})
    else:
        user = None
        #return redirect(login_sucess)        
    return render(request, 'login.html', {'form': LoginStudentForm})

def login_sucess(request):
    return render(request, 'login_sucess.html')
