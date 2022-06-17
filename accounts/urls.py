from django.urls import path 

# import form /procostaMain/accounts/views.py
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('status/<str:no>/', views.status, name="status"),
]