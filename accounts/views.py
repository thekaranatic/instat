from cmath import phase
from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from django.shortcuts import get_object_or_404
from .models import *
from .forms import ProjectForm


# views
def dashboard(request):
    projects = Project.objects.all()

    return render(request, 'accounts/dashboard.html', {'projects':projects})


def status(request, no):
    projects = get_object_or_404(Project, pk=no) 
    
    return render(request, 'accounts/status.html',{'projects':projects})

def addProject(request): 

    form = ProjectForm()
    if request.method == 'GET':   
        # print("Printing POST:", request.POST)
        form = ProjectForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')


    context = {'form': form}
    return render(request, 'accounts/addProject.html', context)