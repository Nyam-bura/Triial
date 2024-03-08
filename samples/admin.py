from django.contrib import admin

from samples.models import CustomerComplaints,ScheduledDirectors,MobileInformation

# Register your models here.
# admin.site.register(AbstractModel)
admin.site.register(CustomerComplaints)
admin.site.register(ScheduledDirectors)    
admin.site.register(MobileInformation)