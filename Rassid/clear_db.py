import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rassid.settings')
django.setup()

from flights.models import Flight, GateAssignment
from passengers.models import PassengerFlight, Passenger

def clear_data():
    print("Clearing PassengerFlight data...")
    count_pf, _ = PassengerFlight.objects.all().delete()
    print(f"Deleted {count_pf} PassengerFlight records.")

    print("Clearing Passenger data...")
    count_p, _ = Passenger.objects.all().delete()
    print(f"Deleted {count_p} Passenger records.")

    print("Clearing GateAssignment data...")
    count_ga, _ = GateAssignment.objects.all().delete()
    print(f"Deleted {count_ga} GateAssignment records.")

    print("Clearing Flight data...")
    count_f, _ = Flight.objects.all().delete()
    print(f"Deleted {count_f} Flight records.")
    
    print("Database cleared successfully.")

if __name__ == "__main__":
    clear_data()
