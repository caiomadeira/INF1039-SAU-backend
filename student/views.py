from django.shortcuts import render
from rest_framework import generics
from .models import AbsencesModel, ClassesModel
from .serializers import AbsencesSerializer, ClassesSerializer

class AbsencesView(generics.ListCreateAPIView):
    queryset = AbsencesModel.objects.all()
    serializer_class = AbsencesSerializer
    
class ClassesView(generics.ListCreateAPIView):
    queryset = ClassesModel.objects.all()
    serializer_class = ClassesSerializer