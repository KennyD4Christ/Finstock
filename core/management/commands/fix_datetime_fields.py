from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from core.models import Customer  # Adjust to your app name

class Command(BaseCommand):
    help = 'Fixes datetime fields stored as strings'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        for customer in customers:
            if isinstance(customer.modified, str):
                customer.modified = parse_datetime(customer.modified)
                customer.save()
        self.stdout.write(self.style.SUCCESS('Successfully fixed datetime fields'))
