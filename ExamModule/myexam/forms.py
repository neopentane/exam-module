from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Choice, Exam, Student, Modules


class StudentRegForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['exam_modules']
        exclude = ['roll_no']
