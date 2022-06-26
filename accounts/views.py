from cmath import phase
from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from sqlalchemy import true
from .models import Project
from django.shortcuts import get_object_or_404
from .models import *
from .forms import ProjectForm
import time
from django.core.mail import send_mail

# views
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'accounts/dashboard.html', {'projects':projects})

def status(request, no):
    projects = get_object_or_404(Project, pk=no) 
    return render(request, 'accounts/status.html',{'projects':projects})

def addProject(request): 
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form. save()
            return render(request, 'accounts/projectAdded.html')

    context={'form':form}
    return render(request, 'accounts/addProject.html', context)


def updateProject(request, no):
    proj = Project.objects.get(id=no)
    form  = ProjectForm(instance=proj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form. save()
            return redirect('/dashboard')
    
    context={'form':form}
    return render(request, 'accounts/updateProject.html', context)

    