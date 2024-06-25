from django.urls import path
from .views import AbsencesView, ClassesView

urlpatterns = [
    path('absences', AbsencesView.as_view(), name="Faltas"),
    path('classes', ClassesView.as_view(), name="Horarios e salas de aula")
]
