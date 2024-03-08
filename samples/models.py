from django.db import models
from django.utils.translation import gettext as _

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("C", "Coporate"),
    ("O","Other"),
)

EDUCATION_CHOICES = (
    ("P", "Primary"),
    ("S", "Secondary"),
    ("T", "Tertiary"),
    ("U", "University"),
    ("C", "College"),
)

CURRENCY_CHOICES = (
    ("K", "Ksh"),
    ("U", "USh"),
    ("T", "TZs"),
)
EXECUTIVE_CHOICES = (
    ("E", "Executive"),
    ("N", "Non-Executive"),
)

IDENTITY_CHOICES = (
    ("I", "ID"),
    ("P", "Passport"),
)


CERTIFICATION_CHOICES = (
    ("P", "PHD"),
    ("M", "MBA"),
    ("B", "BSE"),
)

STATUS_CHOICES = (
    ("P", "Pending"),
    ("C", "Complete"),
)

class AbstractModel(models.Model):
    row_id = models.IntegerField(_("row_id"), blank=False, null=True,default=1)
    psp_id = models.CharField(_("psp_id"), blank=False, null=True, max_length=10,default=1)
    agent_id = models.CharField(_("agent_id"), blank=False, null=True, max_length=10, unique=True)
    reporting_date = models.DateField(_("reporting_date"), blank=False, null=False)
    gender = models.CharField(_("gender"), blank=False, null=False, max_length=5, choices=GENDER_CHOICES)

    class Meta:
        unique_together = ['row_id','psp_id','gender','reporting_date']

    

class CustomerComplaints(models.Model):
    reporting_date = models.DateField(_("reporting_date"), blank=False, null=False)
    complaint_code = models.CharField(_("complaint_code"), blank=False, null=True, max_length=7)
    frequency = models.CharField(_("frequency"), blank=False, null=False, max_length=10)
    complainant_name = models.CharField(_("complainant_name"), blank=False, null=False, max_length=25)
    complainant_age = models.PositiveSmallIntegerField(_("complainant_age"))
    complainant_contact_number = models.CharField(_("complainant_contact_number"),blank=False,null=False,max_length=25,unique=True)
    location = models.CharField(_("location"), max_length=10)
    education_level = models.CharField(_("education_level"), max_length=10, choices=EDUCATION_CHOICES)
    extra_details = models.CharField(_("extra_details"), max_length=255)
    date_of_occurence = models.DateField(_("date_of_occurence"), blank=False, null=False)
    date_resolved = models.DateField(_("date_resolved"), blank=False, null=False)
    status = models.CharField(_("status"), blank=False, null=True, max_length=15, choices=STATUS_CHOICES)
    amount = models.BigIntegerField(_("amount"), blank=False, null=False, default="0")
    currency = models.CharField(_("currency"), max_length=1, choices=CURRENCY_CHOICES, default="0")
    psp_customer_info = models.ForeignKey(AbstractModel,on_delete=models.CASCADE,null=True)

    @property
    def amount_in_ksh(self):
        conversion_rates = {
            "K": 1,
            "U": 0.029,
            "T": 0.22,
        }
        conversion_rate = conversion_rates.get(self.currency)
        if conversion_rate is not None:
            return self.amount * conversion_rate
        else:

            raise ValueError("Invalid Currency Specified")

    def __str__(self):
        return f"{self.amount} {self.currency}"



AGENT_STATUS_CHOICES = (("A", "Active"), ("D", "Dormant"))

class MobileInformation(models.Model):
    favorite_cell = models.CharField(_("favorite_cell"), blank=False, null=False, max_length=10)
    sub_county_code = models.CharField(_("sub_county_code"), blank=False, null=False, max_length=3)
    agent_type_code = models.CharField(_("agent_type_code"), blank=False, null=False, max_length=10)
    agent_status = models.CharField(_("agent_status"), blank=False, null=False, max_length=25, choices=AGENT_STATUS_CHOICES)
    band_code = models.CharField(_("band_code"), blank=False, null=False, max_length=25)
    psp_customer_info = models.ForeignKey(AbstractModel, on_delete=models.CASCADE,null=True)
    cash_in_volume = models.DecimalField(_("cash_volume"), blank=False, null=False, default=0, max_digits=10, decimal_places=2)
    value_cash_in = models.DecimalField(_("value_cash_in"), blank=False, null=False, decimal_places=2, max_digits=10, default=0)
    cash_out_volume = models.DecimalField(_("cash_out_volume"), blank=False, null=False, default=0, decimal_places=2, max_digits=10)
    value_cash_out = models.DecimalField(_("value_cash_out"), blank=False, null=False, default=0, max_digits=10, decimal_places=2)
    float_amount = models.DecimalField(_("float_amount"), blank=False, null=False, default=0, max_digits=10, decimal_places=2)
    agent_cash_deposits = models.DecimalField(_("agent_cash_deposits"), blank=False, null=False, default=0, max_digits=10, decimal_places=2)
    agent_cash_deposits_bank = models.DecimalField(_("agent_cash_deposits_bank"), blank=False, null=False, default=0, max_digits=10, decimal_places=2)
    agent_cash_withdrawal_bank = models.DecimalField(_("agent_cash_withdrawal_bank"), decimal_places=2, blank=False, null=False, default=0, max_digits=10)
    value_agent_cash_withdrawal_bank = models.DecimalField(_("value_agent_cash_withdrawal_bank"), max_digits=10, decimal_places=2, blank=False, null=False, default=0)

class ScheduledDirectors(models.Model):
    psp_customer_info = models.ForeignKey(AbstractModel, on_delete=models.CASCADE,null=True)
    directors_name = models.CharField(_("directors_name"),blank=False,null=False,max_length=255)
    type_of_director = models.CharField(_("type_of_director"),blank=False,null=False,max_length=10,choices=EXECUTIVE_CHOICES)
    date_of_birth = models.DateField(_("date_of_birth"),blank=False,null=False)
    identification_documents = models.CharField(_("identification_documents"),blank=False,null=False,max_length=20,choices=IDENTITY_CHOICES)
    level_of_education = models.CharField(_("level_of_education"),blank=False,null=False,max_length=255,choices=CERTIFICATION_CHOICES)
    directorship_position = models.CharField(_("directorship_position"),blank=False,null=False,max_length=255)
    contact_number = models.CharField(_("contact_number"),blank=False,null=False,max_length=20)
    appointment_date = models.DateField(_("appointment_date"),blank=False,null=False) 
    data_transparency= models.CharField(_("data_transparency"),blank=False,null=False,max_length=255)
    retirement_date = models.DateField(_("retirement_date"),blank=False,null=False,max_length=255)
    start_date = models.DateField(_("start_date"),blank=False,null=False,auto_now=False)
    end_date = models.DateField(_("end_date"),blank=False,null=False)
    pin = models.CharField(_("pin"),blank=False,null=False,max_length=20)

    class Meta:
        unique_together = [["pin","identification_documents"]]

# from datetime import datetime
# from your_app.models import CustomerComplaints

# customer1 = CustomerComplaints(
#     reporting_date=datetime(2002, 2, 20),
#     complaint_code="CB02",
#     frequency="2",
#     complainant_name="Janet",
#     complainant_age=22,
#     complainant_contact_number="01134533190",
#     location="Nairobi",
#     education_level="U",
#     extra_details="She is a genius",
#     date_of_occurrence=datetime(2024, 3, 1),
#     date_resolved=datetime(2024, 3, 2),
#     status="P",
#     amount=100,
#     currency="Ksh",
#     psp_customer_info=1
# )
# customer1.save()
