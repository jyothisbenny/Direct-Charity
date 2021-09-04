from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('patient_request/', views.patient_request, name="patient_request_url"),
                  path('request_readMore/<int:id>', views.request_readMore, name="request_readMore_url"),
                  path('payment/<int:id>', views.payment, name="payment_url"),
                  path('report/<int:id>', views.report, name="report_url"),
                  path('Notifications/', views.notifications, name="message_url"),
                  path('list_payments/', views.listPaymentsForApprove, name="list_payment_url"),
                  path('success_stories/', views.successStories, name="success_stories_url"),
                  path('payment_successful/<int:id>', views.paymentSuccessful, name="payment_successful_url"),
                  path('payment_unsuccessful/<int:id>', views.paymentNotSuccessful, name="payment_unsuccessful_url"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
