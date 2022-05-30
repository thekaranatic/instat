from django.shortcuts import render
from django.http import HttpResponse

# views
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def client(request):
    return HttpResponse("client page")