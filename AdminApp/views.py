from django.shortcuts import render, redirect
from django.contrib import messages
from .models import tbl_admin


# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        admins = tbl_admin.objects.all()
        flag = 0
        for admin in admins:
            if admin.email == email and admin.password == password:
                flag = 1
                return redirect('admin_home_url')
        if flag == 0:
            messages.info(request, 'invalid username and password')
            return redirect('admin_login_url')

    else:
        return render(request, "Admin/AdminLogin.html")


def admin_registration(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if tbl_admin.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register_url')

            else:
                Admin = tbl_admin.objects.create(email=email, password=password1)
                Admin.save()
                messages.success(request, 'Registration Successfully completed, Now please Login!')
                return redirect('admin_login_url')
        else:
            messages.info(request, 'password not matching')
            return redirect('admin_registration_url')

    return render(request, "Admin/AdminRegistration.html")


def admin_home(request):
    return render(request, "Admin/AdminHome.html")
