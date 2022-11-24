from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    gender = forms.ChoiceField(choices=('Male', 'Female'), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'password1', 'password2']

class Create(forms.Form):
    name = forms.CharField(max_length=20)
    
