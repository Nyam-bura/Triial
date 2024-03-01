from rest_framework import serializers
from .models import CustomerComplaints , ScheduledDirectors,MobileInformation, AbstractModel


class CustomerComplaintsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =CustomerComplaints
        fields = '__all__'

class ScheduledDirectorsSerializer(serializers.ModelSerializer):
    pin = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = ScheduledDirectors
        fields = ['complaints','directors_name','type_of_director','date_of_birth','identification_documents','level_of_education',
                  'directorship_position','contact_number','appointment_date','retirement_date','data_transparency','start_date',
                  'end_date','pin']


class MobileInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileInformation
        fields = ['favorite_cell','sub_county_code','agent_type_code','agent_status','band_code','cash_in_volume',
                  'value_cash_in','cash_out_volume','value_cash_out','float_amount','agent_cash_deposits','agent_cash_deposits_bank',
                  'agent_cash_withdrawal_bank','value_agent_cash_withdrawal_bank']


class AbstractSerializer(serializers.ModelSerializer):
    psp_customer_info = CustomerComplaintsSerializer(many=True)
    mobile_psp_info = MobileInformationSerializer(many=True)


    class Meta:
        model = AbstractModel
        fields = ['row_id','reporting_date','gender','psp_customer_info','agent_status','complaints']
        
        def create(self, validated_data):
            print(validated_data)                                                                                               
            try:
                psp_customer_info = validated_data.pop('psp_customer_info')
                psp_customer_info, did_create = ScheduledDirectors.objects.update_or_create(**psp_customer_info)
                print('dnjdfdjfjjrf')
                customer = AbstractModel.objects.update_or_create(psp_customer_info=psp_customer_info, **validated_data)
                mobile_psp_info = validated_data.pop('agent_status')
                for mobile_psp_info in mobile_psp_info:
                    mobile_psp_info.objects.update_or_create(**mobile_psp_info)

                    return customer
            except Exception as e:
                print("Exception occured in method .create in MobileInformationSerializer")
                print(e.args)
                return None
