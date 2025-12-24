import os
import django
from collections import Counter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rassid.settings')
django.setup()

from passengers.models import PassengerFlight

print("Checking for duplicate access_tokens...")
tokens = list(PassengerFlight.objects.values_list('access_token', flat=True))
total = len(tokens)
unique = len(set(tokens))

print(f"Total: {total}, Unique: {unique}")

if total != unique:
    print("Duplicates found! Logic: regenerate all.")
    import uuid
    for pf in PassengerFlight.objects.all():
        pf.access_token = uuid.uuid4()
        pf.save()
    print("Regenerated all tokens.")
else:
    print("No duplicates found. Strange?")
