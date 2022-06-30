from django.urls import path 

# import form /procostaMain/accounts/views.py
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('confirmLogout/', views.confirmLogout, name="confirmLogout"),

    # path('', views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('status/<str:no>/', views.status, name="status"),

    path('addProject/', views.addProject, name="addProject"),
    path('updateProject/<str:no>/', views.updateProject, name="updateProject"),
    path('deleteProject/<str:no>/', views.deleteProject, name="deleteProject"),
]