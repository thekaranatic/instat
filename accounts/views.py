from cmath import phase
from multiprocessing import context
import re
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.shortcuts import get_object_or_404

# views
def dashboard(request):
    projects = Project.objects.all()

    return render(request, 'accounts/dashboard.html', {'projects':projects})


def status(request, no):
    projects = get_object_or_404(Project, pk=no) 
    
    return render(request, 'accounts/status.html',{'projects':projects})

def addProject(request):
    return render(request, 'accounts/addProject.html')