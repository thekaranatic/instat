from django.shortcuts import render
from django.http import HttpResponse

# views
def home(request):
    return render(request, 'accounts/dashboard.html')

def products(request):
    return HttpResponse("products page")

def profile(request):
    return HttpResponse("profile page")

def user(request):
    return HttpResponse("user page")