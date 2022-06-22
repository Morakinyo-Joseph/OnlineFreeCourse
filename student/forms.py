from django import forms
from student.models import *


class StudentsignupForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }