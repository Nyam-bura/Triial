# Generated by Django 5.0.3 on 2024-03-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0006_remove_mobileinformation_psp_customer_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileinformation',
            name='psp_customer_info',
            field=models.CharField(max_length=255, null=True, verbose_name='psp_customer_info'),
        ),
    ]
