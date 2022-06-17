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

    
    if request.method == 'POST':   
        if request.POST.get('proj_name') and request.POST.get('client_name') and request.POST.get('client_email') and request.POST.get('date_initiated') and request.POST.get('ect') and request.POST.get('status') and request.POST.get('collab') and request.POST.get('phase'):
            Project = Project
            Project.p_name = request.POST.get('proj_name')
            Project.c_name = request.POST.get('client_name')
            Project.c_mail = request.POST.get('client_email')
            Project.init_date = request.POST.get('date_initiated')
            Project.ect = request.POST.get('ect')
            Project.status = request.POST.get('status')
            Project.collab = request.POST.get('collab')
            Project.phase = request.POST.get('phase')
            
            Project.save()

            return render(request, 'accounts/addProject.html')
    else:
        return render(request, 'accounts/addProject.html')