import email
from pickle import NONE
import profile
from re import template
from winsound import PlaySound
from django.shortcuts import render, redirect
from accounts.decorators import unauthenticated_user
from .models import Project
from django.shortcuts import get_object_or_404
from .models import *
from .forms import ProjectForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .decorators import unauthenticated_user

# views
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        print('Printing post:', request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            full_name = fname + lname 
            reg_email = form.cleaned_data.get('email')
            reg_username = form.cleaned_data.get('username')
            messages.success(request, 'Account created. Welcome, ' + fname + '!')

            # send mail to confirm the user of his successful registration
            template = render_to_string('accounts/onboard.html', {'fname':fname, 'reg_email':reg_email, 'reg_username':reg_username, 'full_name':full_name})
            
            email = EmailMessage(
                'Welcome aboard' + ' ' + fname + '!',
                template,
                settings.EMAIL_HOST_USER,
                [reg_email],
            )
            email.fail_silently = False
            email.send()
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):
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

def userPage(request):
    return render(request, 'accounts/user.html')

@login_required(login_url='login')
def dashboard(request):
    # '-id' stores greatestToLeast ordered projects
    projects = Project.objects.all().order_by('-id') 
    return render(request, 'accounts/dashboard.html', {'projects':projects})

def status(request, no):
    projects = get_object_or_404(Project, pk=no)
    return render(request, 'accounts/status.html',{'projects':projects})

@login_required(login_url='login')
def miniStats(request):
    from django.db.models import Count #library to count items 

    initiatedCount = Project.objects.filter(project_status="Initiated").count()
    in_progressCount = Project.objects.filter(project_status="In progress").count()
    pausedCount = Project.objects.filter(project_status="Paused").count()
    abortedCount = Project.objects.filter(project_status="Aborted").count()
    completedCount = Project.objects.filter(project_status="Completed").count()

    return render(request, 'accounts/mini_stats.html', {'initiatedCount':initiatedCount, 'in_progressCount':in_progressCount, 'pausedCount':pausedCount, 'abortedCount':abortedCount, 'completedCount':completedCount})

@login_required(login_url='login')
def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        # print('printing post:', request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

            pname = form.cleaned_data.get('project_name')
            c_email = form.cleaned_data.get('client_mail')
            template = render_to_string('accounts/client_email.html', {'pname':pname, 'c_email':c_email})

            email = EmailMessage(
                'Your project' + ' ' + pname + ' ' + ' is initiated!',
                template,
                # 'http://127.0.0.1:8000/status/' + id,
                settings.EMAIL_HOST_USER,
                [c_email]
            )
            email.fail_silently = False
            email.send()
            # return redirect('/dashboard')

            return render(request, 'messages/projectAdded.html')
    
    context = {'form':form}
    return render(request, 'forms/addProject.html', context)

def new_func(request):
    if request.user.is_authenticated():
        fname = request.user.first_name
        lname = request.user.first_name
    return fname,lname

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteProject(request, no):
    proj = Project.objects.get(id=no)

    if request.method == 'POST':
        proj.delete()
        return redirect('/dashboard')


    context = {'item':proj}
    return render(request, 'prompt/deleteProject.html', context)