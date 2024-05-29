from rest_framework import serializers
from .models import AbsencesModel, ClassesModel

class AbsencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsencesModel
        fields = ["id", "code", "name", "count", "last_update"]
        
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassesModel
        fields = ["id", "code", "name", "hours", "last_update"]