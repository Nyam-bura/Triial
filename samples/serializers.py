from rest_framework import serializers
from .models import CustomerComplaints , ScheduledDirectors,MobileInformation, AbstractModel

class AbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractModel
        fields = ['row_id','psp_id','agent_id','reporting_date','gender']


class CustomerComplaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerComplaints
        fields = ['reporting_date','complaint_code','frequency','complainant_name','complainant_age','complainant_contact_number','location','education_level','extra_details',
              'date_of_occurence','date_resolved','status','amount','currency','psp_customer_info']

class ScheduledDirectorsSerializer(serializers.ModelSerializer):
    pin = serializers.CharField(write_only=False,style={'input_type':'password'})
    class Meta:
        model = ScheduledDirectors
        fields = ['psp_customer_info','directors_name','type_of_director','date_of_birth','identification_documents','level_of_education','directorship_position',
                  'contact_number','appointment_date','data_transparency','retirement_date','start_date','end_date','pin']

class MobileInformationSerializer(serializers.ModelSerializer):
    # psp_customer_info = CustomerComplaintsSerializer(many=True)
    class Meta:
        model= MobileInformation
        fields = ['psp_customer_info','favorite_cell','sub_county_code','agent_type_code','agent_status','band_code','cash_in_volume','value_cash_in','cash_out_volume',
                  'value_cash_out','float_amount','agent_cash_deposits','agent_cash_deposits_bank','agent_cash_withdrawal_bank','value_agent_cash_withdrawal_bank']

        # def create(self, validated_data):
        #     customers_data = validated_data.pop('psp_customer_info')
        #     mobile = MobileInformation.objects.create(**validated_data)
        #     for customer_data in customers_data:
        #         CustomerComplaintsSerializer.create(mobile=mobile,**customer_data)
