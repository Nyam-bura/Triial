from django.contrib import admin

from samples.models import CustomerComplaints,ScheduledDirectors,MobileInformation,AbstractModel

# Register your models here.
class AbstractModelAdmin(admin.ModelAdmin):
    model = AbstractModel
    list_display = ['row_id','psp_id','agent_id','reporting_date','gender']

admin.site.register(AbstractModel,AbstractModelAdmin)



class CustomerComplaintsAdmin(admin.ModelAdmin):
    model = CustomerComplaints
    list_display = ['complaint_code','frequency','complainant_name','complainant_age','complainant_contact_number','location','education_level','extra_details','date_of_occurence'
                    ,'date_resolved','status','amount','currency']
admin.site.register(CustomerComplaints,CustomerComplaintsAdmin)


class ScheduledDirectorsAdmin(admin.ModelAdmin):
    model = ScheduledDirectors
    list_display = [
        'directors_name','type_of_director','date_of_birth','identification_documents','level_of_education',
        'directorship_position','contact_number','appointment_date','retirement_date','data_transparency','start_date',
        'end_date','pin'
    ]

admin.site.register(ScheduledDirectors,ScheduledDirectorsAdmin)


class MobileInformationAdmin(admin.ModelAdmin):
    model = MobileInformation
    list_display = ['favorite_cell','sub_county_code','agent_type_code','agent_status','band_code','cash_in_volume','value_cash_in','cash_out_volume','value_cash_out','float_amount',
                    'agent_cash_deposits','agent_cash_deposits_bank','agent_cash_withdrawal_bank','value_agent_cash_withdrawal_bank']

admin.site.register(MobileInformation,MobileInformationAdmin)    
