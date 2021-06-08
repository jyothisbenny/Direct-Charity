from django.shortcuts import redirect, render
from django.contrib import messages
from .models import UsersProfile
from .utils import send_sms
import random


# Create your views here.

# registration
def user_registration(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if UsersProfile.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('user_registration_url')
            elif UsersProfile.objects.filter(username=username).exists():
                messages.info(request, 'username already taken, try another one')
                return redirect('user_registration_url')
            elif UsersProfile.objects.filter(phone=phone).exists():
                messages.info(request, 'phone number already exists, try login')
                return redirect('user_registration_url')
            else:
                User = UsersProfile.objects.create(first_name=first_name, last_name=last_name, username=username,
                                                   email=email, phone=phone, password=password2)
                User.save()
                return redirect('user_login_url')
        else:
            messages.info(request, "password not matching")
    return render(request, "User/UserRegistration.html")


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        users = UsersProfile.objects.all()
        flag = 0
        for user in users:
            if user.email == email and user.password == password:
                flag = 1
                if not user.phone_verified:
                    # send sms function
                    otp = random.randrange(100000, 999999)
                    print("otp is", otp)
                    user.otp = otp
                    user.save()
                    send_sms(otp, user.phone)
                    if user is not None:
                        request.session['pk'] = user.pk
                        return redirect('user_otpVerify_url')

                else:
                    return redirect('user_registration_url')
        if flag == 0:
            messages.info(request, 'invalid username and password')
            return redirect('user_login_url')

    else:
        return render(request, 'User/UserLogin.html')


def user_otpverify(request):
    if request.method == "POST":
        user_entry = request.POST['userentry']

        pk = request.session.get('pk')
        user = UsersProfile.objects.get(pk=pk)
        if int(user_entry) == user.otp:
            print("hey")
            return redirect('user_home_url')
        else:
            messages.info(request, "invalid otp please type the 6 digit otp")
            return redirect('user_otpVerify_url')

    return render(request, 'User/UserOtpVerify.html')


def user_home(request):
    return render(request, 'User/UserHome.html')
