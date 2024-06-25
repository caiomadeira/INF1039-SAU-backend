from django import forms
from student.models import Student

class LoginStudentForm(forms.ModelForm):
    username = forms.TextInput()
    password = forms.PasswordInput()
    class Meta:
        model = Student
        fields = ['username', 'password']