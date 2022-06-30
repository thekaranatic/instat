from django.shortcuts import render, redirect
from .models import Project
from django.shortcuts import get_object_or_404
from .models import *
from .forms import ProjectForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

# views
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                fname = form.cleaned_data.get('first_name')
                messages.success(request, 'Account created. Welcome, ' + fname + '!')

                return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def confirmLogout(request):
    return render(request, 'prompt/logoutUser.html')

# @login_required(login_url='login')
def dashboard(request):
    projects = Project.objects.all()
    return render(request, 'accounts/dashboard.html', {'projects':projects})

def status(request, no):
    projects = get_object_or_404(Project, pk=no) 
    return render(request, 'accounts/status.html',{'projects':projects})

# @login_required(login_url='login')
def addProject(request): 
    form = ProjectForm()
    if request.method == 'POST':
        # print('printing post:', request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('/dashboard')

            return render(request, 'messages/projectAdded.html')

    context = {'form':form}
    return render(request, 'forms/addProject.html', context)

# @login_required(login_url='login')
def updateProject(request, no):
    proj = Project.objects.get(id=no)
    form  = ProjectForm(instance=proj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=proj)
        if form.is_valid():
            form.save()
            # return redirect('/dashboard')
            return render(request, 'messages/projectUpdated.html')
    
    context = {'form':form}
    return render(request, 'forms/updateProject.html', context)

# @login_required(login_url='login')
def deleteProject(request, no):
    proj = Project.objects.get(id=no)

    if request.method == 'POST':
        proj.delete()
        return redirect('/dashboard')


    context = {'item':proj}
    return render(request, 'prompt/deleteProject.html', context)