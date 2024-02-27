from django.urls import path
from .views import CustomerComplaintsApiView,ScheduledDirectorsApiView,MobileInformationApiView
from samples import views


app_name = 'samples'

urlpatterns = [
    path('customer/', CustomerComplaintsApiView.as_view(), name='customer'),
    # path('customer/<int:id>/', customer_complaints, name='customer_complaints'),
    path('director/', ScheduledDirectorsApiView.as_view(), name='director'),
    # path('director/<int:id>/', director_details, name='director_details'),
    path('mobile/', MobileInformationApiView.as_view(), name='mobile'),
]
