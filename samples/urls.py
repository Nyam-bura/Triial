from django.urls import path
from .views import CustomerComplaintsViewSet,ScheduledDirectorsViewSet,MobileInformationViewSet
from samples import views

app_name = 'samples'

urlpatterns = [
    path('customer/', CustomerComplaintsViewSet.as_view({'get':'list'}), name='customer'),
    path('customer/<int:id>/',views.customer_details),
    path('director/', ScheduledDirectorsViewSet.as_view({'get':'list'}), name='director'),
    path('director/<int:id>/',views.director_details),
    path('mobile/<int:id>/',views.mobile_details),
    path('mobile/', MobileInformationViewSet.as_view({'get':'list'}), name='mobile'),
]
