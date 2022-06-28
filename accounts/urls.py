from django.urls import path 

# import form /procostaMain/accounts/views.py
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),


    path('', views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('status/<str:no>/', views.status, name="status"),

    path('addProject/', views.addProject, name="addProject"),
    path('updateProject/<str:no>/', views.updateProject, name="updateProject"),
    path('deleteProject/<str:no>/', views.deleteProject, name="deleteProject"),
]