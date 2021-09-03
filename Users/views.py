from django.shortcuts import redirect, render
from django.contrib import messages
from .models import MyUser
from Patients.models import Patient, SuccessStories
from .utils import send_sms
import random

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

from .forms import NewUserForm
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')


def user_registration(request):
    args = {}
    if request.method == "POST":
        form = NewUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!, Now please Login")
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
            user.phone_verified = True
            user.save()
            return redirect('user_home_url')
        else:
            messages.info(request, "invalid otp please type the 6 digit otp")
            return redirect('user_otpVerify_url')

    return render(request, 'User/UserOtpVerify.html')


def LogoutView(request):
    auth.logout(request)
    return redirect('index_url')


@login_required()
def user_home(request):
    patients = Patient.objects.all()
    for i in patients:
        if i.collected_amount >= i.required_amount:

            SuccessStories.objects.create(owner=i.owner, patient_name=i.patient_name, relationship=i.relationship,
                                          patient_photo=i.patient_photo, disease=i.disease, category=i.category,
                                          description=i.description, documents=i.documents, hospital=i.hospital,
                                          doctor_name=i.doctor_name, required_amount=i.required_amount,
                                          upi_id=i.upi_id, collected_amount=i.collected_amount, admin_verified=i.admin_verified,
                                          report_count=i.report_count)
            i.delete()

    user_requests = Patient.objects.filter(admin_verified=True).filter(report_count__lte=18)
    print(type(user_requests))
    return render(request, 'User/UserHome.html', {'user_requests': user_requests})
