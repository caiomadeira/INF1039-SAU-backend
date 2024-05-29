from django.db import models
from django.contrib.auth.models import User

# Isso aqui deve ficar claro com o modelo conceitual UML


# Create your models here.

# Essa model talvez seja redundante
class SAUStudent(models.Model):
    #owner=models.ForeignKey(to=User, on_delete=models.CASCADE)
    pass
    
    
# Model referente a materias
class CollegeSubjects(models.Model):
    #name = models.CharField()
    pass

