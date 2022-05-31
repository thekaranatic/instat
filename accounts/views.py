from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# views
def dashboard(request):
    projects = Project.objects.all()

    return render(request, 'accounts/dashboard.html', {'projects':projects})


def client(request):
    return HttpResponse("client page")