# Generated by Django 5.0.3 on 2024-03-15 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0005_remove_mobileinformation_mobile_psp_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobileinformation',
            name='psp_customer_info',
        ),
        migrations.AlterField(
            model_name='customercomplaints',
            name='psp_customer_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='samples.mobileinformation'),
        ),
    ]
