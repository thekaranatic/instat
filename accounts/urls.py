from django.urls import path 

# import form /procostaMain/accounts/views.py
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('dashboard/', views.dashboard),
    path('status/<int:no>/', views.status),
    
]