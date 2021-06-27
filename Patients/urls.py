from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('patient_request/', views.patient_request, name="patient_request_url"),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
