from django import forms
from student.models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput()
        }