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
import time
from django.core.mail import send_mail

# views
def dashboard(request):
    projects = Project.objects.all()
    
    send_mail(
            'hello from instat onboarding bot',
            'KAY KAY LAVDYA | GENERATED FROM DJANGO WSGI SERVER',
            'instat.onboard@gmail.com',
            ['karankakati24@gmail.com'],
            fail_silently=False
        )

    return render(request, 'accounts/dashboard.html', {'projects':projects})

def status(request, no):
    projects = get_object_or_404(Project, pk=no) 
    
    return render(request, 'accounts/status.html',{'projects':projects})

def addProject(request): 

    form = ProjectForm()
    if request.method == 'POST':   
        p_name = request.POST['proj_name']
        c_name = request.POST['client_name']
        c_mail = request.POST['client_email']
        init_date = request.POST['date_initiated']
        ect = request.POST['ect']
        p_status = request.POST['status']
        collabs = request.POST['collab']
        phase = request.POST['phase']

        proj  = Project(
            p_name=p_name,
            c_name=c_name,
            c_mail=c_mail,
            init_date=init_date,
            ect=ect,
            p_status=p_status,
            collabs=collabs,
            phase=phase,
        )

        proj.save()

        # return HttpResponse("Project added!")
        return render(request, 'accounts/projectAdded.html')

        

    else:
        return render(request, 'accounts/addProject.html')

def updateProject(request, no):
    proj = Project.objects.get(id=no)
    form  = ProjectForm(instance=proj)
    
    return render(request, 'accounts/addProject.html', {'form':form})

    