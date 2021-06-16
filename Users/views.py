from django.shortcuts import redirect, render
from django.contrib import messages
from .models import MyUser
from .utils import send_sms
import random

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

from .forms import NewUserForm


# Create your views here.

# # registration
# def user_registration(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         phone1= "+91" + phone
#         if password1 == password2:
#             if MyUser.objects.filter(email=email).exists():
#                 messages.info(request, 'email already exists')
#                 return redirect('user_registration_url')
#             elif MyUser.objects.filter(username=username).exists():
#                 messages.info(request, 'username already taken, try another one')
#                 return redirect('user_registration_url')
#             elif MyUser.objects.filter(phone=phone).exists():
#                 messages.info(request, 'phone number already exists, try login')
#                 return redirect('user_registration_url')
#             else:
#                 User = MyUser.objects.create(first_name=first_name, last_name=last_name, username=username,
#                                                    email=email, phone=phone1, password=password2)
#                 User.save()
#                 return redirect('user_login_url')
#         else:
#             messages.info(request, "password not matching")
#     return render(request, "User/UserRegistration.html")

def user_registration(request):
    args = {}
    if request.method == "POST":
        form = NewUserForm(request.POST)
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


@login_required()
def user_home(request):
    return render(request, 'User/UserHome.html')
