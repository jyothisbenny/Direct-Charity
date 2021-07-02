from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Patient
from .forms import RequestForm, PaymentForm
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

    form = RequestForm
    args['form'] = form.errors
    return render(request=request, template_name="Patients/patients_registration.html",
                  context={"PatientRequest_Form": form})


def request_readMore(request, id):
    patient = Patient.objects.get(pk=id)

    if patient:
        return render(request, "Patients/Request_ReadMore.html", {"patient": patient})


def payment(request, id):
    patient = Patient.objects.get(pk=id)
    need = patient.required_amount - patient.collected_amount
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            print("-----------------------------------hey")
            thought = form.save(commit=False)
            thought.donor = request.user
            thought.patient_id = patient.id
            form.save()
            patient.collected_amount = patient.collected_amount + thought.amount
            patient.save()
            messages.success(request, "Details are submitted successfully")
            return redirect("payment_url", patient.id)
        else:
            print("-----------------------------------hello")
            return render(request=request, template_name="Patients/Payment.html",
                          context={'Payment_Form': form, "patient": patient, "need": need})
    # if request.method == "GET":
    #     return render(request, "Patients/Payment.html", {"patient": patient})
    form = PaymentForm
    return render(request=request, template_name="Patients/Payment.html",
                  context={'Payment_Form': form, "patient": patient, "need": need})


def report(request, id):
    req = Patient.objects.get(id=id)
    if request.method == "POST":



    req.r
    eport_count
    return render(request, "Patients/report.html")
