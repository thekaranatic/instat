import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.shortcuts import get_object_or_404
from json import dumps

# views
def dashboard(request):
    projects = Project.objects.all()

    return render(request, 'accounts/dashboard.html', {'projects':projects})


def status(request, no):
    projects = get_object_or_404(Project, pk=no) 

    dataJSON = dumps(projects)
    return render(request, 'accounts/status.html', {'projects':projects}, {'data':dataJSON})