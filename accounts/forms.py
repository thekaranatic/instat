from typing import Text
from django import forms
from django.forms import ModelForm, TextInput
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'p_name': forms.TextInput(attrs={'class':'form-control'}),
            'c_name': forms.TextInput(attrs={'class':'form-control'}),
            'c_mail': forms.EmailInput(attrs={'class':'form-control'}),
            'c_mail': forms.EmailInput(attrs={'class':'form-control'}),
        }


