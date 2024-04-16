from django.core.management.base import BaseCommand
from Samples.models import AbstractModel, MobileInformation
import csv
import requests
from io import StringIO

class Command(BaseCommand):
    help = 'Send data to another API daily at 22:00'

    def handle(self, **args):
        url = 'https://eobjk3bc0hu19p1.m.pipedream.net'

        csv_data = StringIO()
        data_list = MobileInformation.objects.all().values()  
        csv_writer = csv.DictWriter(csv_data, fieldnames=data_list[0].keys())
        csv_writer.writeheader()        
        csv_writer.writerows(data_list)

        csv_data.seek(0)

        response = requests.post(url, data=csv_data)

        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS(f'Data Successfully Sent to API'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to send data to API'))