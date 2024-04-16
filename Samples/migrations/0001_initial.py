# Generated by Django 5.0.4 on 2024-04-12 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_cell', models.CharField(max_length=10, verbose_name='favorite_cell')),
                ('sub_county_code', models.CharField(max_length=3, verbose_name='sub_county_code')),
                ('agent_type_code', models.CharField(max_length=10, verbose_name='agent_type_code')),
                ('psp_customer_info_id', models.CharField(max_length=255, null=True, verbose_name='psp_customer_info_id')),
                ('agent_status', models.CharField(choices=[('A', 'Active'), ('D', 'Dormant')], max_length=25, verbose_name='agent_status')),
                ('band_code', models.CharField(max_length=25, verbose_name='band_code')),
                ('cash_in_volume', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='cash_volume')),
                ('value_cash_in', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='value_cash_in')),
                ('cash_out_volume', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='cash_out_volume')),
                ('value_cash_out', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='value_cash_out')),
                ('float_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='float_amount')),
                ('agent_cash_deposits', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='agent_cash_deposits')),
                ('agent_cash_deposits_bank', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='agent_cash_deposits_bank')),
                ('agent_cash_withdrawal_bank', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='agent_cash_withdrawal_bank')),
                ('value_agent_cash_withdrawal_bank', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='value_agent_cash_withdrawal_bank')),
            ],
        ),
        migrations.CreateModel(
            name='AbstractModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.IntegerField(default=1, null=True, verbose_name='row_id')),
                ('psp_id', models.CharField(default=1, max_length=10, null=True, verbose_name='psp_id')),
                ('agent_id', models.CharField(max_length=10, null=True, unique=True, verbose_name='agent_id')),
                ('reporting_date', models.DateField(verbose_name='reporting_date')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Coporate'), ('O', 'Other')], max_length=5, verbose_name='gender')),
            ],
            options={
                'unique_together': {('row_id', 'psp_id', 'gender', 'reporting_date')},
            },
        ),
        migrations.CreateModel(
            name='CustomerComplaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporting_date', models.DateField(verbose_name='reporting_date')),
                ('complaint_code', models.CharField(max_length=7, null=True, verbose_name='complaint_code')),
                ('frequency', models.CharField(max_length=10, verbose_name='frequency')),
                ('complainant_name', models.CharField(max_length=25, verbose_name='complainant_name')),
                ('complainant_age', models.PositiveSmallIntegerField(verbose_name='complainant_age')),
                ('complainant_contact_number', models.CharField(max_length=25, unique=True, verbose_name='complainant_contact_number')),
                ('location', models.CharField(max_length=10, verbose_name='location')),
                ('education_level', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('T', 'Tertiary'), ('U', 'University'), ('C', 'College')], max_length=10, verbose_name='education_level')),
                ('extra_details', models.CharField(max_length=255, verbose_name='extra_details')),
                ('date_of_occurence', models.DateField(verbose_name='date_of_occurence')),
                ('date_resolved', models.DateField(verbose_name='date_resolved')),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete')], max_length=15, null=True, verbose_name='status')),
                ('amount', models.BigIntegerField(default='0', verbose_name='amount')),
                ('currency', models.CharField(choices=[('K', 'Ksh'), ('U', 'USh'), ('T', 'TZs')], default='0', max_length=1, verbose_name='currency')),
                ('psp_customer_info_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='Samples.mobileinformation')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledDirectors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directors_name', models.CharField(max_length=255, verbose_name='directors_name')),
                ('type_of_director', models.CharField(choices=[('E', 'Executive'), ('N', 'Non-Executive')], max_length=10, verbose_name='type_of_director')),
                ('date_of_birth', models.DateField(verbose_name='date_of_birth')),
                ('identification_documents', models.CharField(choices=[('I', 'ID'), ('P', 'Passport')], max_length=20, verbose_name='identification_documents')),
                ('level_of_education', models.CharField(choices=[('P', 'PHD'), ('M', 'MBA'), ('B', 'BSE')], max_length=255, verbose_name='level_of_education')),
                ('directorship_position', models.CharField(max_length=255, verbose_name='directorship_position')),
                ('contact_number', models.CharField(max_length=20, verbose_name='contact_number')),
                ('appointment_date', models.DateField(verbose_name='appointment_date')),
                ('data_transparency', models.CharField(max_length=255, verbose_name='date_transparency')),
                ('retirement_date', models.DateField(max_length=255, verbose_name='retirement_date')),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('pin', models.CharField(max_length=20, verbose_name='pinn')),
                ('psp_customer_info_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Samples.abstractmodel')),
            ],
        ),
    ]