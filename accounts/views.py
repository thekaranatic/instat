from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import Project
from django.shortcuts import get_object_or_404
from .models import *
from .forms import ProjectForm

# views
def register(request):
    context = {}
    return render(request, 'accounts/register.html', context)

def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'accounts/dashboard.html', {'projects':projects})

def status(request, no):
    projects = get_object_or_404(Project, pk=no) 
    return render(request, 'accounts/status.html',{'projects':projects})

def addProject(request): 
    form = ProjectForm()
    if request.method == 'POST':
        # print('printing post:', request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/dashboard')

            return render(request, 'accounts/projectAdded.html')

    context = {'form':form}
    return render(request, 'accounts/addProject.html', context)

def updateProject(request, no):
    proj = Project.objects.get(id=no)
    form  = ProjectForm(instance=proj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            # return redirect('/dashboard')
            return render(request, 'accounts/projectUpdated.html')
    
    context = {'form':form}
    return render(request, 'accounts/updateProject.html', context)

def deleteProject(request, no):
    proj = Project.objects.get(id=no)

    if request.method == 'POST':
        proj.delete()
        return redirect('/dashboard')


    context = {'item':proj}
    return render(request, 'accounts/deleteProject.html', context)