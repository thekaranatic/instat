from django.urls import path 

# import form /procostaMain/accounts/views.py
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('products/', views.products),
    path('profile/', views.profile),
    path('user/', views.user)
]