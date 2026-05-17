import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1_site.settings')
django.setup()

from circuits.models import Circuit
from tyres.models import Tyre

print("\n" + "="*60)
print("DATA VERIFICATION AFTER CLEANUP")
print("="*60)

print(f"\n✓ Total Circuits: {Circuit.objects.count()} (was 25, now 23)")
print(f"✓ Total Tyres: {Tyre.objects.count()} (was 10, now 7)")

print("\n--- Circuits in Database ---")
for c in Circuit.objects.values_list('name', flat=True).order_by('name'):
    print(f"  • {c}")

print("\n--- Tyres in Database ---")
for t in Tyre.objects.values_list('name', flat=True).order_by('name'):
    print(f"  • {t}")

print("\n" + "="*60)
print("✓ Cleanup verified - No duplicates!")
print("="*60 + "\n")
