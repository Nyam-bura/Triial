# Generated by Django 5.0.3 on 2024-03-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0007_mobileinformation_psp_customer_info'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='abstractmodel',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='abstractmodel',
            name='psp_customer_info',
            field=models.CharField(max_length=255, null=True, verbose_name='psp_customer_info'),
        ),
        migrations.AlterUniqueTogether(
            name='abstractmodel',
            unique_together={('psp_customer_info',)},
        ),
    ]
