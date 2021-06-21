from django.urls import path
from . import views

urlpatterns = [
    path('patient_request/', views.patient_request, name="patient_request_url"),
        ]
