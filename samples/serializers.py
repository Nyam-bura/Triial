from rest_framework import serializers
from .models import CustomerComplaints , ScheduledDirectors,MobileInformation, AbstractModel

class Abstract(serializers.ModelSerializer):
    class Meta:
        model = CustomerComplaints
        fields = "__all__"

class CustomerComplaintsSerializer(serializers.ModelSerializer):
    psp_customer_info = Abstract(many=True,read_only=True)
    class Meta:AbstractModel
    model =CustomerComplaints
    fields = "__all__"

class ScheduledDirectorsSerializer(serializers.ModelSerializer):
    pin = serializers.CharField(write_only=False,style={'input_type':'password'})
    class Meta:
        model = ScheduledDirectors
        fields = "__all__"
        
class MobileInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model= MobileInformation
        fields = "__all__"
        
