from django.core.management.base import BaseCommand
from datetime import date
from drivers.models import Driver
from seasons.models import Season, SeasonResult
from records.models import Record
from terminology.models import TerminologyTerm

class Command(BaseCommand):
    help = 'Add more F1 data: drivers, seasons, records, and terminology (does NOT delete existing data)'

    def handle(self, *args, **options):
        self.add_drivers()
        self.add_seasons()
        self.add_records()
        self.add_terminology()
        
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

    def add_terminology(self):
        self.stdout.write('\n--- Adding Terminology Terms ---')
        new_terminology = [
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
            {
                'term': 'Apex',
                'definition': 'The point in a corner where the car is closest to the inside edge of the track.',
                'category': 'Racing'
            },
            {
                'term': 'Chassis',
                'definition': 'The structural frame of the car that supports all components and the driver.',
                'category': 'Technical'
            },
            {
                'term': 'DRS',
                'definition': 'Drag Reduction System used to reduce aerodynamic drag and improve overtaking.',
                'category': 'Technical'
            },
            {
                'term': 'Drag',
                'definition': 'Aerodynamic resistance that slows the car down, especially on straight sections.',
                'category': 'Technical'
            },
            {
                'term': 'Downforce',
                'definition': 'Aerodynamic force that pushes the car onto the track to increase grip through corners.',
                'category': 'Technical'
            },
            {
                'term': 'Fuel Mix',
                'definition': 'Engine setting that adjusts power output and fuel efficiency during the race.',
                'category': 'Technical'
            },
            {
                'term': 'Full Course Yellow',
                'definition': 'A caution condition where the whole track is under yellow flag and drivers must slow down.',
                'category': 'Safety'
            },
            {
                'term': 'Green Flag',
                'definition': 'The signal that normal racing has resumed after a caution or formation lap.',
                'category': 'Racing'
            },
            {
                'term': 'Ground Effect',
                'definition': 'The aerodynamic principle where low pressure under the car generates downforce.',
                'category': 'Technical'
            },
            {
                'term': 'Heel-and-Toe',
                'definition': 'A driving technique that allows simultaneous braking and downshifting smoothly.',
                'category': 'Technical'
            },
            {
                'term': 'Hot Lap',
                'definition': 'A fast lap used to set a quick time in qualifying or test car performance in race trim.',
                'category': 'Racing'
            },
            {
                'term': 'Parc Fermé',
                'definition': 'The restricted area and conditions after qualifying where car setup changes are limited.',
                'category': 'Regulation'
            },
            {
                'term': 'Pit Lane Speed Limit',
                'definition': 'The maximum allowed speed in the pit lane to protect mechanics and other personnel.',
                'category': 'Safety'
            },
            {
                'term': 'Pole Position',
                'definition': 'The first starting position on the grid, awarded to the fastest qualifier.',
                'category': 'Racing'
            },
            {
                'term': 'Qualifying',
                'definition': 'The timed session that determines the starting order for the race.',
                'category': 'Racing'
            },
            {
                'term': 'Safety Car',
                'definition': 'A vehicle that leads the field at reduced speed during dangerous track conditions.',
                'category': 'Safety'
            },
            {
                'term': 'Scrutineering',
                'definition': 'The technical inspection of cars before and after sessions to ensure regulation compliance.',
                'category': 'Regulation'
            },
            {
                'term': 'Slipstream',
                'definition': 'The aerodynamic tow created behind another car that reduces drag and can aid overtaking.',
                'category': 'Racing'
            },
            {
                'term': 'Split Time',
                'definition': 'An intermediate lap time used to compare performance across different sections of the track.',
                'category': 'Racing'
            },
            {
                'term': 'Sectors',
                'definition': 'Divisions of the track used to measure and compare performance throughout a lap.',
                'category': 'Racing'
            },
            {
                'term': 'Sprint Race',
                'definition': 'A shorter race format that usually takes place on Saturday during a Grand Prix weekend.',
                'category': 'Racing'
            },
            {
                'term': 'Telemetry',
                'definition': 'Live data transmitted from the car to the team for performance analysis and strategy decisions.',
                'category': 'Technical'
            },
            {
                'term': 'Tyre Compound',
                'definition': 'The rubber mixture used in a tyre, which affects grip, durability, and performance.',
                'category': 'Technical'
            },
            {
                'term': 'Tyre Warmers',
                'definition': 'Equipment used to heat tyres before they are fitted to the car for optimal grip and performance.',
                'category': 'Technical'
            },
            {
                'term': 'Virtual Safety Car',
                'definition': 'A race neutralization system that requires drivers to slow to a prescribed delta time without a physical safety car.',
                'category': 'Safety'
            },
            {
                'term': 'Weight Distribution',
                'definition': 'The balance of mass between the front and rear of the car, affecting handling and stability.',
                'category': 'Technical'
            },
            {
                'term': 'Yellow Flag',
                'definition': 'A caution signal indicating danger on track and prohibiting overtaking in the affected sector.',
                'category': 'Safety'
            },
            {
                'term': 'Blue Flag',
                'definition': 'A signal shown to a slower car to let a faster car through without impeding it.',
                'category': 'Regulation'
            },
            {
                'term': 'Black Flag',
                'definition': 'A penalty signal ordering a driver to return to the pits and retire from the session.',
                'category': 'Regulation'
            },
            {
                'term': 'Red Flag',
                'definition': 'A signal that the session is stopped immediately due to a serious incident or unsafe track conditions.',
                'category': 'Safety'
            },
            {
                'term': 'Slip Angle',
                'definition': 'The angle between the direction a tyre is pointed and the actual direction the car is moving.',
                'category': 'Technical'
            },
        ]

        for term_data in new_terminology:
            term, created = TerminologyTerm.objects.get_or_create(
                term=term_data['term'],
                defaults=term_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {term.term}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {term.term}')
