from django.shortcuts import redirect, render
from django.contrib import messages
from .models import MyUser
from Patients.models import Patients
from .utils import send_sms
import random

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

from .forms import NewUserForm


def user_registration(request):
    args = {}
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user_login_url")
        else:
            return render(request=request, template_name="User/UserRegistration.html", context={'register_form': form})
            # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    args['form'] = form.errors
    return render(request=request, template_name="User/UserRegistration.html", context={"register_form": form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if not user.phone_verified:
                # send sms function
                otp = random.randrange(100000, 999999)
                print("otp is", otp)
                user.otp = otp
                user.save()
                print("---------------------------------------------------", user.phone)
                print("type", type(user.phone))
                send_sms(otp, user.phone)
                if user is not None:
                    request.session['pk'] = user.pk
                    return redirect('user_otpVerify_url')

            else:
                return redirect('user_home_url')
        else:
            messages.info(request, 'invalid username and password')
            return redirect('user_login_url')

    else:
        return render(request, 'User/UserLogin.html')


def user_otpverify(request):
    if request.method == "POST":
        user_entry = request.POST['userentry']

        pk = request.session.get('pk')
        user = MyUser.objects.get(pk=pk)
        # print("-----------------------------", user.otp)
        # print("-----------------------------", user_entry)
        if int(user_entry) == int(user.otp):
            print("hey")
            user.phone_verified = True
            user.save()
            return redirect('user_home_url')
        else:
            messages.info(request, "invalid otp please type the 6 digit otp")
            return redirect('user_otpVerify_url')

    return render(request, 'User/UserOtpVerify.html')


def LogoutView(request):
    auth.logout(request)
    return redirect('user_login_url')


@login_required(login_url='user_login_url')
def user_home(request):
    User_requests = Patients.objects.filter(admin_verified=True)
    return render(request, 'User/UserHome.html', {'user_requests': User_requests})


