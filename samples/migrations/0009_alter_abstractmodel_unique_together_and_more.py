# Generated by Django 5.0.3 on 2024-03-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0008_alter_abstractmodel_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='abstractmodel',
            unique_together={('row_id', 'psp_id', 'gender', 'reporting_date')},
        ),
        migrations.AlterField(
            model_name='scheduleddirectors',
            name='data_transparency',
            field=models.CharField(max_length=255, verbose_name='date_transparency'),
        ),
        migrations.RemoveField(
            model_name='abstractmodel',
            name='psp_customer_info',
        ),
    ]
