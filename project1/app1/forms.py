from django import forms
from django.contrib.auth.models import User
from .import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password','first_name','last_name',]
        widgets={
            'password':forms.PasswordInput(),
            'email':forms.EmailInput()
                }
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65)
    widgets={
        'password':forms.PasswordInput(),
    }