from django import forms
from Home.models import Department
from django.contrib.auth.models import User
from .models import Student,Teacher

class Dep_form(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,  
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['department','first_name', 'last_name', 'email', 'phone_number', 'age', 'address']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['department','first_name', 'last_name','qualification', 'email', 'phone_number', 'age', 'address']
