from django.core.management.base import BaseCommand
from circuits.models import Circuit
from tyres.models import Tyre

class Command(BaseCommand):
    help = 'Clean up duplicate circuits and tyres from the database'

    def handle(self, *args, **options):
        self.stdout.write("\n" + "="*60)
        self.stdout.write("CLEANUP: Removing Duplicate Circuits & Tyres")
        self.stdout.write("="*60 + "\n")

        # Clean up duplicate circuits
        self.stdout.write("--- Removing Duplicate Circuits ---")
        
        # Remove: "Autodromo di Monza" (keep "Autodromo Nazionale di Monza")
        monza_dup = Circuit.objects.filter(name="Autodromo di Monza")
        if monza_dup.exists():
            count = monza_dup.count()
            monza_dup.delete()
            self.stdout.write(self.style.SUCCESS(f"  ✓ Removed {count} duplicate: Autodromo di Monza"))
        
        # Remove: "Autodromo José María Gutiérrez" (keep "Autodromo Hermanos Rodríguez")
        mexico_dup = Circuit.objects.filter(name="Autodromo José María Gutiérrez")
        if mexico_dup.exists():
            count = mexico_dup.count()
            mexico_dup.delete()
            self.stdout.write(self.style.SUCCESS(f"  ✓ Removed {count} duplicate: Autodromo José María Gutiérrez"))

        # Clean up duplicate tyres
        self.stdout.write("\n--- Removing Duplicate Tyres ---")
        
        # Remove: "Hard Compound" (keep "Pirelli P Zero Hard")
        hard_dup = Tyre.objects.filter(name="Hard Compound")
        if hard_dup.exists():
            count = hard_dup.count()
            hard_dup.delete()
            self.stdout.write(self.style.SUCCESS(f"  ✓ Removed {count} duplicate: Hard Compound"))
        
        # Remove: "Medium Compound" (keep "Pirelli P Zero Medium")
        medium_dup = Tyre.objects.filter(name="Medium Compound")
        if medium_dup.exists():
            count = medium_dup.count()
            medium_dup.delete()
            self.stdout.write(self.style.SUCCESS(f"  ✓ Removed {count} duplicate: Medium Compound"))
        
        # Remove: "Intermediate" (keep "Pirelli P Zero Intermediate")
        inter_dup = Tyre.objects.filter(name="Intermediate")
        if inter_dup.exists():
            count = inter_dup.count()
            inter_dup.delete()
            self.stdout.write(self.style.SUCCESS(f"  ✓ Removed {count} duplicate: Intermediate"))

        self.stdout.write("\n" + "="*60)
        self.stdout.write(self.style.SUCCESS("✓ Cleanup Complete - All Duplicates Removed!"))
        self.stdout.write("="*60 + "\n")
