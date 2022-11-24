from django import forms
from .models import *

class Signup(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.PasswordInput()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=("Male", "Female"))
    position = forms.CharField(max_length=50)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customers
        