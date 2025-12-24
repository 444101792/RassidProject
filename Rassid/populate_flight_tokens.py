import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rassid.settings')
django.setup()

from passengers.models import PassengerFlight

print("Populating unique access_tokens for PassengerFlights...")
count = 0
for pf in PassengerFlight.objects.all():
    if not pf.access_token:
        pf.access_token = uuid.uuid4()
        pf.save()
        count += 1
    
print(f"Updated {count} records.")
