from django.urls import path
from . import views

urlpatterns = [
    path('userlogin/', views.user_login, name="user_login_url"),
    path('userreg/', views.user_registration, name="user_registration_url"),
    path('otpverify/', views.user_otpverify, name="user_otpVerify_url"),
    path('userhome/', views.user_home, name="user_home_url"),
    path('logout/', views.LogoutView, name="user_logout_url"),
]
