from django.core.management.base import BaseCommand
from circuits.models import Circuit

class Command(BaseCommand):
    help = 'Add more F1 circuits to the database (does NOT delete existing data)'

    def handle(self, *args, **options):
        self.stdout.write('\n--- Adding Circuits ---')
        new_circuits = [
            {
                'name': 'Suzuka International Racing Course',
                'country': 'Japan',
                'city': 'Suzuka',
                'length_km': 5.807,
                'turns': 18,
                'drs_zones': 2,
                'first_gp_year': 1976,
                'lap_record_time': '1:27.064',
                'lap_record_holder': 'Sebastian Vettel',
                'lap_record_year': 2018,
                'bio': 'Suzuka is one of the most iconic circuits, famous for the 130R corner and figure-eight layout.'
            },
            {
                'name': 'Marina Bay Street Circuit',
                'country': 'Singapore',
                'city': 'Singapore',
                'length_km': 5.285,
                'turns': 23,
                'drs_zones': 2,
                'first_gp_year': 2008,
                'lap_record_time': '1:41.905',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2018,
                'bio': 'Singapore is a night race featuring tight streets, slow corners, and challenging conditions.'
            },
            {
                'name': 'Baku City Circuit',
                'country': 'Azerbaijan',
                'city': 'Baku',
                'length_km': 6.003,
                'turns': 20,
                'drs_zones': 2,
                'first_gp_year': 2016,
                'lap_record_time': '1:42.872',
                'lap_record_holder': 'Charles Leclerc',
                'lap_record_year': 2019,
                'bio': 'Baku is a modern street circuit combining high-speed straights with tight technical sections.'
            },
            {
                'name': 'Yas Island',
                'country': 'United Arab Emirates',
                'city': 'Abu Dhabi',
                'length_km': 5.554,
                'turns': 21,
                'drs_zones': 3,
                'first_gp_year': 2009,
                'lap_record_time': '1:23.862',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2021,
                'bio': 'Yas Island often hosts the season finale with modern facilities and challenging racing.'
            },
            {
                'name': 'Autodromo José María Gutiérrez',
                'country': 'Mexico',
                'city': 'Mexico City',
                'length_km': 4.304,
                'turns': 17,
                'drs_zones': 2,
                'first_gp_year': 1962,
                'lap_record_time': '1:16.901',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2017,
                'bio': 'Mexico City circuit is known for high altitude and unpredictable weather affecting strategy.'
            },
            {
                'name': 'Autódromo José Carlos Pace',
                'country': 'Brazil',
                'city': 'São Paulo',
                'length_km': 4.309,
                'turns': 15,
                'drs_zones': 2,
                'first_gp_year': 1990,
                'lap_record_time': '1:14.932',
                'lap_record_holder': 'Juan Pablo Montoya',
                'lap_record_year': 2004,
                'bio': 'Interlagos is a challenging circuit with elevation changes and weather variations affecting races.'
            },
            {
                'name': 'Istanbul Park',
                'country': 'Turkey',
                'city': 'Istanbul',
                'length_km': 5.338,
                'turns': 14,
                'drs_zones': 2,
                'first_gp_year': 2005,
                'lap_record_time': '1:24.770',
                'lap_record_holder': 'Max Verstappen',
                'lap_record_year': 2020,
                'bio': 'Istanbul Park features the famous Turn 8 with high lateral forces demanding from drivers and tyres.'
            },
            {
                'name': 'Shanghai International Circuit',
                'country': 'China',
                'city': 'Shanghai',
                'length_km': 5.451,
                'turns': 16,
                'drs_zones': 2,
                'first_gp_year': 2004,
                'lap_record_time': '1:31.497',
                'lap_record_holder': 'Sebastian Vettel',
                'lap_record_year': 2019,
                'bio': 'Shanghai hosts one of the fastest circuits with smooth tarmac and high-speed corners.'
            },
            {
                'name': 'Sepang International Circuit',
                'country': 'Malaysia',
                'city': 'Kuala Lumpur',
                'length_km': 5.543,
                'turns': 15,
                'drs_zones': 2,
                'first_gp_year': 1999,
                'lap_record_time': '1:28.772',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2017,
                'bio': 'Sepang features hot weather, high humidity, and dramatic weather conditions challenging drivers.'
            },
            {
                'name': 'Autodromo Hermanos Rodríguez',
                'country': 'Mexico',
                'city': 'Mexico City',
                'length_km': 4.304,
                'turns': 17,
                'drs_zones': 2,
                'first_gp_year': 1963,
                'lap_record_time': '1:16.901',
                'lap_record_holder': 'Max Verstappen',
                'lap_record_year': 2022,
                'bio': 'This historic Mexican circuit has been hosting international motorsport events for decades.'
            },
            {
                'name': 'Autodromo di Monza',
                'country': 'Italy',
                'city': 'Monza',
                'length_km': 5.793,
                'turns': 11,
                'drs_zones': 3,
                'first_gp_year': 1950,
                'lap_record_time': '1:19.556',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2020,
                'bio': 'Monza is the temple of speed with legendary straights and the passionate Italian tifosi.'
            },
            {
                'name': 'Circuit Paul Ricard',
                'country': 'France',
                'city': 'Le Castellet',
                'length_km': 5.842,
                'turns': 15,
                'drs_zones': 2,
                'first_gp_year': 1971,
                'lap_record_time': '1:32.740',
                'lap_record_holder': 'Max Verstappen',
                'lap_record_year': 2023,
                'bio': 'Paul Ricard features modern facilities with run-off areas and a combination of fast and technical sections.'
            },
            {
                'name': 'Circuit of the Americas',
                'country': 'United States',
                'city': 'Austin',
                'length_km': 5.515,
                'turns': 20,
                'drs_zones': 3,
                'first_gp_year': 2012,
                'lap_record_time': '1:32.910',
                'lap_record_holder': 'Max Verstappen',
                'lap_record_year': 2023,
                'bio': 'COTA is located in Austin, Texas with a unique layout featuring elevation changes and varied corners.'
            },
            {
                'name': 'Autodromo di Mugello',
                'country': 'Italy',
                'city': 'Scarperia',
                'length_km': 5.245,
                'turns': 15,
                'drs_zones': 2,
                'first_gp_year': 1920,
                'lap_record_time': '1:17.632',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2020,
                'bio': 'Mugello is a high-speed circuit with fast-flowing corners and historic significance.'
            },
            {
                'name': 'Algarve International Circuit',
                'country': 'Portugal',
                'city': 'Portimão',
                'length_km': 4.653,
                'turns': 15,
                'drs_zones': 1,
                'first_gp_year': 2020,
                'lap_record_time': '1:18.750',
                'lap_record_holder': 'Lewis Hamilton',
                'lap_record_year': 2020,
                'bio': 'Portimão is a challenging circuit with elevation changes and spectacular Portuguese scenery.'
            },
        ]

        for circuit_data in new_circuits:
            circuit, created = Circuit.objects.get_or_create(
                name=circuit_data['name'],
                defaults=circuit_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {circuit.name}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {circuit.name}')

        self.stdout.write(self.style.SUCCESS('\n✓ All circuits added successfully! No existing data was affected.'))
