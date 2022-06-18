from typing import Text
from django import forms
from django.forms import ModelForm, TextInput
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



