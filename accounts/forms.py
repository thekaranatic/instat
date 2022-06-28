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
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

