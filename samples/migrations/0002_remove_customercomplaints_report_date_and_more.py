# Generated by Django 5.0.2 on 2024-02-22 08:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customercomplaints',
            name='report_date',
        ),
        migrations.AlterField(
            model_name='customercomplaints',
            name='amount_lost',
            field=models.BigIntegerField(verbose_name='amount_lost'),
        ),
        migrations.AlterField(
            model_name='customercomplaints',
            name='amount_recovered',
            field=models.BigIntegerField(verbose_name='amount_recovered'),
        ),
        migrations.AlterField(
            model_name='customercomplaints',
            name='reporting_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='reporting_date'),
        ),
    ]
