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

        widgets = {
            'project_name': forms.TextInput(attrs={'class': 'form', 'id':'proj_name', 'required':'required'}),
            'client_name': forms.TextInput(attrs={'class': 'form', 'id':'client_name','required':'required'}),
            'client_mail': forms.EmailInput(attrs={'class': 'form', 'id':'client_email','required':'required'}),
            'project_initiated_on': forms.DateInput(attrs={'class': 'form','id':'date_initiated', 'required':'required'}),
            'ect': forms.DateInput(attrs={'class': 'form', 'id':'ect','required':'required'}),
            'project_status': forms.TextInput(attrs={'class': 'form', 'id':'status-dropdown','required':'required'}),
            'collaborations': forms.NumberInput(attrs={'class': 'form', 'id':'collab','required':'required'}),
            'phase': forms.NumberInput(attrs={'class': 'form', 'id':'phase','required':'required'}),
        }

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

       

