from django.urls import path
from . import views

urlpatterns = [
    path('adminlogin/', views.admin_login, name="admin_login_url"),
    path('adminreg/', views.admin_registration, name="admin_registration_url"),
    path('adminhome/', views.admin_home, name="admin_home_url")
    ]