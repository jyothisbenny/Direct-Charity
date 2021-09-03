from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Patient, Report, Payment, SuccessStories
from .forms import RequestForm, PaymentForm, ReportForm
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


@login_required(login_url='user_login_url')
def request_readMore(request, id):
    patient = Patient.objects.get(pk=id)

    if patient:
        return render(request, "Patients/Request_ReadMore.html", {"patient": patient})


"""view for payments"""


@login_required(login_url='user_login_url')
def payment(request, id):
    req = Patient.objects.get(pk=id)
    need = req.required_amount - req.collected_amount
    if request.method == "POST":
        form = PaymentForm(request.POST, request.FILES)

        if form.is_valid():
            print("-----------------------------------hey")
            thought = form.save(commit=False)
            thought.donor = request.user
            thought.patient_id = req.id
            form.save()
            req.collected_amount = req.collected_amount + thought.amount
            req.save()
            messages.success(request, "Details are submitted successfully")
            return redirect("payment_url", req.id)
        else:
            print("-----------------------------------hello")
            return render(request=request, template_name="Patients/Payment.html",
                          context={'Payment_Form': form, "patient": req, "need": need})
    # if request.method == "GET":
    #     return render(request, "Patients/Payment.html", {"patient": patient})
    form = PaymentForm
    return render(request=request, template_name="Patients/Payment.html",
                  context={'Payment_Form': form, "patient": req, "need": need})


"""view for reporting a patient request """


@login_required(login_url='user_login_url')
def report(request, id):
    req = Patient.objects.get(id=id)
    rep = Report.objects.filter(patient_id=id)
    for r in rep:
        if r.reporter_id == request.user.id:
            messages.info(request, "You already reported this user!")
            return redirect("request_readMore_url", req.id)

    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            print("-----------------------------------hey")
            kk = form.save(commit=False)
            kk.reporter = request.user
            kk.patient_id = req.id
            form.save()
            req.report_count = req.report_count + 1
            req.save()
            messages.success(request, "Reported successfully")
            return redirect("request_readMore_url", req.id)
        else:
            print("-----------------------------------hello")
            return render(request=request, template_name="Patients/Report.html",
                          context={'Report_Form': form, "patient": req})

    form = ReportForm
    return render(request=request, template_name="Patients/Report.html",
                  context={'Report_Form': form, "patient": req})


@login_required(login_url='user_login_url')
def notifications(request):
    dict = {}
    """getting payments made by the login ed user"""
    pay = Payment.objects.filter(donor=request.user.id)
    for i in pay:
        """getting patients where reported by more than 5 users"""
        pat = Patient.objects.filter(id=i.patient.id).filter(report_count__gte=2)
        if pat:
            dict[i] = pat

    pay2 = Payment.objects.filter(donor=request.user.id)
    for j in pay2:
        """getting patients where reported by more than 5 users"""
        pat2 = SuccessStories.objects.filter(id=j.patient.id).filter(report_count__gte=2)
        if pat2:
            dict[j] = pat2

    print("++++++++++", dict)
    return render(request, 'Patients/Messages.html', {'patients': dict})


def listPaymentsForApprove(request):
    dict1 = {}
    """getting patient requests made by the login ed user"""
    pat = Patient.objects.filter(owner=request.user.id)
    for i in pat:
        """getting all the payments are made for the patients"""
        pay = Payment.objects.filter(patient_id=i.id)
        for j in pay:
            print("------------------------hey-------", j)
            print("-----------------hello----------------")
            dict1[i] = j
    # print("$$$$$$$$$$$$$$$$$$$$$$", pat)

    print("++++++++++", dict1)
    return render(request, "Patients/ListPayment.html", {'payments': dict1})


def successStories(request):
    success_stories = SuccessStories.objects.filter(admin_verified=True)
    return render(request, 'Patients/successStories.html', {'success_stories': success_stories})