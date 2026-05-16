from django.core.management.base import BaseCommand
from datetime import date
from drivers.models import Driver
from seasons.models import Season, SeasonResult
from records.models import Record
from glossary.models import GlossaryTerm

class Command(BaseCommand):
    help = 'Add more F1 data: drivers, seasons, records, and glossary (does NOT delete existing data)'

    def handle(self, *args, **options):
        self.add_drivers()
        self.add_seasons()
        self.add_records()
        self.add_glossary()
        
        self.stdout.write(self.style.SUCCESS('\n✓ All data added successfully! No existing data was affected.'))

    def add_drivers(self):
        self.stdout.write('\n--- Adding Drivers ---')
        new_drivers = [
            {
                'name': 'Giancarlo Fisichella',
                'nationality': 'Brazil',
                'date_of_birth': date(1973, 1, 25),
                'driver_number': 8,
                'abbreviation': 'FIS',
                'races': 308,
                'wins': 3,
                'podiums': 41,
                'pole_positions': 1,
                'fastest_laps': 2,
                'championships': 0,
                'bio': 'Giancarlo Fisichella is a Brazilian driver with a long F1 career and strong performances.',
                'debut_year': 1996
            },
            {
                'name': 'Jarno Trulli',
                'nationality': 'Italy',
                'date_of_birth': date(1977, 7, 13),
                'driver_number': 4,
                'abbreviation': 'TRU',
                'races': 256,
                'wins': 1,
                'podiums': 32,
                'pole_positions': 14,
                'fastest_laps': 3,
                'championships': 0,
                'bio': 'Jarno Trulli is an Italian driver known for his qualifying speed and precision.',
                'debut_year': 1997
            },
            {
                'name': 'Giancarlo Giovanardi',
                'nationality': 'Italy',
                'date_of_birth': date(1975, 1, 5),
                'driver_number': 9,
                'abbreviation': 'GIO',
                'races': 28,
                'wins': 0,
                'podiums': 0,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Giancarlo Giovanardi competed in Formula 1 with determination and skill.',
                'debut_year': 2004
            },
            {
                'name': 'Romain Grosjean',
                'nationality': 'France',
                'date_of_birth': date(1986, 4, 17),
                'driver_number': 8,
                'abbreviation': 'GRO',
                'races': 200,
                'wins': 0,
                'podiums': 10,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Romain Grosjean is a French driver known for aggressive driving and racecraft.',
                'debut_year': 2009
            },
            {
                'name': 'Pastor Maldonado',
                'nationality': 'Venezuela',
                'date_of_birth': date(1985, 3, 9),
                'driver_number': 13,
                'abbreviation': 'MAL',
                'races': 96,
                'wins': 1,
                'podiums': 1,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Pastor Maldonado is a Venezuelan driver who achieved a Grand Prix victory.',
                'debut_year': 2011
            },
            {
                'name': 'Mark Webber',
                'nationality': 'Australia',
                'date_of_birth': date(1976, 8, 27),
                'driver_number': 2,
                'abbreviation': 'WEB',
                'races': 308,
                'wins': 9,
                'podiums': 122,
                'pole_positions': 16,
                'fastest_laps': 41,
                'championships': 0,
                'bio': 'Mark Webber is an Australian driver with an impressive F1 career and many podiums.',
                'debut_year': 2002
            },
            {
                'name': 'Felipe Nasr',
                'nationality': 'Brazil',
                'date_of_birth': date(1992, 8, 21),
                'driver_number': 12,
                'abbreviation': 'NAR',
                'races': 45,
                'wins': 0,
                'podiums': 1,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Felipe Nasr is a Brazilian driver competing with talent and determination.',
                'debut_year': 2014
            },
            {
                'name': 'Esteban Gutierrez',
                'nationality': 'Mexico',
                'date_of_birth': date(1991, 8, 5),
                'driver_number': 21,
                'abbreviation': 'GUT',
                'races': 73,
                'wins': 0,
                'podiums': 0,
                'pole_positions': 0,
                'fastest_laps': 0,
                'championships': 0,
                'bio': 'Esteban Gutierrez is a Mexican driver bringing his country\'s talent to F1.',
                'debut_year': 2013
            },
        ]

        for driver_data in new_drivers:
            driver, created = Driver.objects.get_or_create(
                name=driver_data['name'],
                defaults=driver_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {driver.name}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {driver.name}')

    def add_seasons(self):
        self.stdout.write('\n--- Adding Seasons ---')
        new_seasons = [
            {
                'year': 2021,
                'drivers_champion': 'Max Verstappen',
                'constructors_champion': 'Mercedes',
                'total_races': 22,
                'description': '2021 season featuring competitive battles and a dramatic championship finale.'
            },
            {
                'year': 2020,
                'drivers_champion': 'Lewis Hamilton',
                'constructors_champion': 'Mercedes',
                'total_races': 17,
                'description': '2020 season shortened due to COVID-19 with Mercedes dominating the grid.'
            },
            {
                'year': 2019,
                'drivers_champion': 'Lewis Hamilton',
                'constructors_champion': 'Mercedes',
                'total_races': 21,
                'description': '2019 season showing Mercedes\' dominance and strong performances.'
            },
        ]

        for season_data in new_seasons:
            season, created = Season.objects.get_or_create(
                year=season_data['year'],
                defaults=season_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {season.year}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {season.year}')

    def add_records(self):
        self.stdout.write('\n--- Adding Records ---')
        new_records = [
            {
                'category': 'driver',
                'title': 'Most Fastest Laps',
                'value': '64',
                'holder': 'Lewis Hamilton',
                'year': 2024,
                'description': 'Lewis Hamilton holds the record for most fastest lap points.'
            },
            {
                'category': 'driver',
                'title': 'Youngest World Champion',
                'value': '23 years 290 days',
                'holder': 'Sebastian Vettel',
                'year': 2010,
                'description': 'Sebastian Vettel became the youngest F1 world champion in 2010.'
            },
            {
                'category': 'race',
                'title': 'Most Consecutive Points Finishes',
                'value': '24 races',
                'holder': 'Sergio Perez',
                'year': 2022,
                'description': 'Sergio Perez achieved 24 consecutive races scoring points.'
            },
            {
                'category': 'constructor',
                'title': 'Most Consecutive Championship Wins',
                'value': '7 titles',
                'holder': 'Mercedes',
                'year': 2020,
                'description': 'Mercedes won 7 consecutive constructor championships (2014-2020).'
            },
            {
                'category': 'race',
                'title': 'Most Podiums in a Career',
                'value': '202',
                'holder': 'Lewis Hamilton',
                'year': 2024,
                'description': 'Lewis Hamilton has achieved the most podium finishes in F1 history.'
            },
            {
                'category': 'driver',
                'title': 'Most Points in a Season',
                'value': '473',
                'holder': 'Max Verstappen',
                'year': 2022,
                'description': 'Max Verstappen scored a record 473 points in the 2022 season.'
            },
        ]

        for record_data in new_records:
            record, created = Record.objects.get_or_create(
                title=record_data['title'],
                defaults=record_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {record.title}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {record.title}')

    def add_glossary(self):
        self.stdout.write('\n--- Adding Glossary Terms ---')
        new_glossary = [
            {
                'term': 'Brake Balance',
                'definition': 'The adjustment of braking force distribution between front and rear wheels.',
                'category': 'Technical'
            },
            {
                'term': 'Fuel Flow',
                'definition': 'The rate at which fuel is consumed by the engine during a race, regulated by FIA.',
                'category': 'Technical'
            },
            {
                'term': 'Hybrid Power Unit',
                'definition': 'Modern F1 engines combining internal combustion with electric motor assistance.',
                'category': 'Technical'
            },
            {
                'term': 'Undercut',
                'definition': 'A pit stop strategy where a driver pits earlier than their competitor to gain track position.',
                'category': 'Racing'
            },
            {
                'term': 'Overcut',
                'definition': 'A pit stop strategy where a driver pits later than their competitor to gain an advantage.',
                'category': 'Racing'
            },
            {
                'term': 'Traction Control',
                'definition': 'A system that limits wheel spin on acceleration by managing engine power delivery.',
                'category': 'Technical'
            },
            {
                'term': 'Flatspot',
                'definition': 'A flat worn area on a tyre from locked wheels or heavy braking, affecting performance.',
                'category': 'Technical'
            },
            {
                'term': 'Racing Line',
                'definition': 'The optimal path through corners that maximizes speed and minimizes lap time.',
                'category': 'Racing'
            },
            {
                'term': 'Understeer',
                'definition': 'A handling condition where the front tyres lose grip before the rear, pushing wide.',
                'category': 'Technical'
            },
            {
                'term': 'Oversteer',
                'definition': 'A handling condition where the rear tyres lose grip before the front, causing sliding.',
                'category': 'Technical'
            },
            {
                'term': 'Formation Lap',
                'definition': 'The warm-up lap before the race start where drivers prepare their cars.',
                'category': 'Racing'
            },
            {
                'term': 'Grand Chelem',
                'definition': 'Achieving pole position, fastest lap, and winning a race in the same weekend.',
                'category': 'Racing'
            },
        ]

        for term_data in new_glossary:
            term, created = GlossaryTerm.objects.get_or_create(
                term=term_data['term'],
                defaults=term_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {term.term}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {term.term}')
