from dataclasses import field, fields
from typing import Text
from django import forms
from django.forms import ModelForm
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class CreateUserForm(UserCreationForm):

    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Re-enter password'}),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required':'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required':'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required':'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required':'required'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
        }

       

