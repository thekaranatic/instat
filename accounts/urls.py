from django.urls import path 

# import form /instatMain/accounts/views.py
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('confirmLogout/', views.confirmLogout, name="confirmLogout"),
    path('user/', views.userPage, name="userPage"),
    
    path('', views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('status/<str:no>/', views.status, name="status"),
    path('miniStats/', views.miniStats, name="miniStats"),

    path('addProject/', views.addProject, name="addProject"),
    path('updateProject/<str:no>/', views.updateProject, name="updateProject"),
    path('deleteProject/<str:no>/', views.deleteProject, name="deleteProject"),

    path('noMobAccess/', views.noMobAccess, name="noMobAccess"),
]