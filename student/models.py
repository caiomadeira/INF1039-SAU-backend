from django.db import models

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