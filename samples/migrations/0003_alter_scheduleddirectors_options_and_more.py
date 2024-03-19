# Generated by Django 5.0.3 on 2024-03-15 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_alter_abstractmodel_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scheduleddirectors',
            options={'ordering': ['pin', 'identification_documents']},
        ),
        migrations.AlterField(
            model_name='customercomplaints',
            name='psp_customer_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mobile', to='samples.abstractmodel'),
        ),
    ]