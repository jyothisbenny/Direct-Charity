from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Patients
from .forms import RequestForm
from django.contrib import messages
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your views here.


@login_required(login_url='user_login_url')
def patient_request(request):
    args = {}
    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)

        if form.is_valid():
            print("-----------------------------------hey")
            thought = form.save(commit=False)
            thought.owner = request.user
            form.save()
            messages.success(request, "request will be posted after admin approves")
            return redirect("user_home_url")
        else:
            print("-----------------------------------hello")
            return render(request=request, template_name="Patients/patients_registration.html",
                          context={'PatientRequest_Form': form})
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RequestForm
    args['form'] = form.errors
    return render(request=request, template_name="Patients/patients_registration.html",
                  context={"PatientRequest_Form": form})
