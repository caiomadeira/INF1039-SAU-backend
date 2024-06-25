from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

class Student(models.Model):
    username = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.title

class AbsencesModel(models.Model):
    code = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    count = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class ClassesModel(models.Model):
    code = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    hours = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title