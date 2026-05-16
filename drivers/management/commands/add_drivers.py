from django.core.management.base import BaseCommand
from datetime import date
from drivers.models import Driver

class Command(BaseCommand):
    help = 'Add new F1 drivers to the database (does NOT delete existing data)'

    def handle(self, *args, **options):
        new_drivers = [
            {
                'name': 'Logan Sargeant',
                'nationality': 'United States',
                'date_of_birth': date(2000, 12, 31),
                'driver_number': 2,
                'abbreviation': 'SAR',
                'races': 40,
                'wins': 0,
                'podiums': 0,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Logan Sargeant is an American driver bringing representation to Formula 1.',
                'debut_year': 2023
            },
            {
                'name': 'Daniel Ricciardo',
                'nationality': 'Australia',
                'date_of_birth': date(1989, 7, 1),
                'driver_number': 3,
                'abbreviation': 'RIC',
                'races': 350,
                'wins': 8,
                'podiums': 56,
                'pole_positions': 0,
                'fastest_laps': 15,
                'championships': 0,
                'bio': 'Daniel Ricciardo is an experienced driver known for his aggressive racing style and smooth racecraft.',
                'debut_year': 2011
            },
            {
                'name': 'Valtteri Bottas',
                'nationality': 'Finland',
                'date_of_birth': date(1989, 8, 28),
                'driver_number': 77,
                'abbreviation': 'BOT',
                'races': 280,
                'wins': 10,
                'podiums': 70,
                'pole_positions': 17,
                'fastest_laps': 20,
                'championships': 0,
                'bio': 'Valtteri Bottas is an experienced Finnish driver known for consistency and reliability.',
                'debut_year': 2013
            },
            {
                'name': 'Zhou Guanyu',
                'nationality': 'China',
                'date_of_birth': date(1999, 5, 30),
                'driver_number': 24,
                'abbreviation': 'ZHO',
                'races': 65,
                'wins': 0,
                'podiums': 0,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Zhou Guanyu is a Chinese driver competing in Formula 1.',
                'debut_year': 2022
            },
            {
                'name': 'Sebastian Vettel',
                'nationality': 'Germany',
                'date_of_birth': date(1987, 7, 3),
                'driver_number': 5,
                'abbreviation': 'VET',
                'races': 300,
                'wins': 53,
                'podiums': 122,
                'pole_positions': 57,
                'fastest_laps': 40,
                'championships': 4,
                'bio': 'Sebastian Vettel is a four-time world champion known for his racecraft and consistency.',
                'debut_year': 2007
            },
            {
                'name': 'Jenson Button',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1983, 1, 19),
                'driver_number': 22,
                'abbreviation': 'BUT',
                'races': 306,
                'wins': 15,
                'podiums': 50,
                'pole_positions': 8,
                'fastest_laps': 8,
                'championships': 1,
                'bio': 'Jenson Button is a former world champion known for his smooth driving style.',
                'debut_year': 2000
            },
            {
                'name': 'Kimi Räikkönen',
                'nationality': 'Finland',
                'date_of_birth': date(1979, 10, 17),
                'driver_number': 7,
                'abbreviation': 'RAI',
                'races': 346,
                'wins': 21,
                'podiums': 103,
                'pole_positions': 18,
                'fastest_laps': 46,
                'championships': 1,
                'bio': 'Kimi Räikkönen is a legendary Finnish driver with one world championship and a record-breaking career.',
                'debut_year': 2001
            },
            {
                'name': 'Juan Pablo Montoya',
                'nationality': 'Colombia',
                'date_of_birth': date(1975, 9, 20),
                'driver_number': 12,
                'abbreviation': 'MON',
                'races': 223,
                'wins': 16,
                'podiums': 67,
                'pole_positions': 30,
                'fastest_laps': 32,
                'championships': 0,
                'bio': 'Juan Pablo Montoya is a talented Colombian driver known for his aggressive racing style.',
                'debut_year': 2001
            },
            {
                'name': 'Rubens Barrichello',
                'nationality': 'Brazil',
                'date_of_birth': date(1972, 7, 23),
                'driver_number': 6,
                'abbreviation': 'BAR',
                'races': 326,
                'wins': 11,
                'podiums': 68,
                'pole_positions': 14,
                'fastest_laps': 17,
                'championships': 0,
                'bio': 'Rubens Barrichello is a Brazilian driver with the most F1 starts in history.',
                'debut_year': 1992
            },
            {
                'name': 'David Coulthard',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1971, 3, 27),
                'driver_number': 17,
                'abbreviation': 'COU',
                'races': 247,
                'wins': 13,
                'podiums': 65,
                'pole_positions': 12,
                'fastest_laps': 19,
                'championships': 0,
                'bio': 'David Coulthard is a British driver known for his consistency and strong performances.',
                'debut_year': 1994
            },
            {
                'name': 'Felipe Massa',
                'nationality': 'Brazil',
                'date_of_birth': date(1981, 4, 25),
                'driver_number': 19,
                'abbreviation': 'MAS',
                'races': 272,
                'wins': 11,
                'podiums': 41,
                'pole_positions': 15,
                'fastest_laps': 12,
                'championships': 0,
                'bio': 'Felipe Massa is a talented Brazilian driver with strong racecraft and determination.',
                'debut_year': 2002
            },
        ]

        for driver_data in new_drivers:
            driver, created = Driver.objects.get_or_create(
                name=driver_data['name'],
                defaults=driver_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✓ Added driver: {driver.name}'))
            else:
                self.stdout.write(f'⊘ Driver already exists: {driver.name}')

        self.stdout.write(self.style.SUCCESS('\nDone! Only new drivers were added.'))
