from django import forms
from .models import *

class Create(forms.Form):
    name = forms.CharField(label="Employee name", max_length=20)
    email = forms.EmailField(label="Email", max_length=30)
    password = forms.CharField(label="password", max_length=20)
    nb = forms.IntegerField(label="Employee ID")
    jobtitle = forms.CharField(label="Job Title", max_length=30)
    legal = forms.BooleanField(label="Legal")
    salary = forms.IntegerField(label="Salary")
