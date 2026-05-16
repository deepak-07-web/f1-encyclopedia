from django.core.management.base import BaseCommand
from seasons.models import Season, SeasonResult
from records.models import Record
from glossary.models import GlossaryTerm
from tyres.models import Tyre

class Command(BaseCommand):
    help = 'Add comprehensive final details: constructor standings, more records, glossary, and tyres (does NOT delete existing data)'

    def handle(self, *args, **options):
        self.add_constructor_standings()
        self.add_more_records()
        self.add_more_glossary()
        self.add_more_tyres()
        
        self.stdout.write(self.style.SUCCESS('\n✓✓✓ All comprehensive final details added successfully! ✓✓✓\n'))

    def add_constructor_standings(self):
        self.stdout.write('\n--- Adding Constructor Standings ---')
        constructor_standings = {
            2025: [
                {'position': 1, 'team': 'Red Bull Racing', 'points': 850},
                {'position': 2, 'team': 'McLaren', 'points': 800},
                {'position': 3, 'team': 'Ferrari', 'points': 710},
                {'position': 4, 'team': 'Mercedes', 'points': 570},
                {'position': 5, 'team': 'Aston Martin', 'points': 220},
                {'position': 6, 'team': 'Alpine', 'points': 85},
                {'position': 7, 'team': 'Haas', 'points': 110},
                {'position': 8, 'team': 'RB F1 Team', 'points': 75},
                {'position': 9, 'team': 'Williams', 'points': 45},
                {'position': 10, 'team': 'Kicksauber', 'points': 20},
            ],
            2024: [
                {'position': 1, 'team': 'McLaren', 'points': 668},
                {'position': 2, 'team': 'Red Bull Racing', 'points': 650},
                {'position': 3, 'team': 'Ferrari', 'points': 735},
                {'position': 4, 'team': 'Mercedes', 'points': 521},
                {'position': 5, 'team': 'Aston Martin', 'points': 207},
                {'position': 6, 'team': 'Alpine', 'points': 53},
                {'position': 7, 'team': 'Haas', 'points': 84},
                {'position': 8, 'team': 'RB F1 Team', 'points': 53},
                {'position': 9, 'team': 'Williams', 'points': 4},
                {'position': 10, 'team': 'Kicksauber', 'points': 0},
            ],
            2023: [
                {'position': 1, 'team': 'Red Bull Racing', 'points': 880},
                {'position': 2, 'team': 'Mercedes', 'points': 746},
                {'position': 3, 'team': 'Ferrari', 'points': 746},
                {'position': 4, 'team': 'McLaren', 'points': 367},
                {'position': 5, 'team': 'Aston Martin', 'points': 90},
                {'position': 6, 'team': 'Alpine', 'points': 34},
                {'position': 7, 'team': 'Haas', 'points': 34},
                {'position': 8, 'team': 'Alfa Romeo', 'points': 15},
                {'position': 9, 'team': 'Williams', 'points': 8},
                {'position': 10, 'team': 'RB F1 Team', 'points': 0},
            ],
            2022: [
                {'position': 1, 'team': 'Red Bull Racing', 'points': 759},
                {'position': 2, 'team': 'Ferrari', 'points': 613},
                {'position': 3, 'team': 'Mercedes', 'points': 487},
                {'position': 4, 'team': 'Alpine', 'points': 173},
                {'position': 5, 'team': 'McLaren', 'points': 122},
                {'position': 6, 'team': 'Alfa Romeo', 'points': 55},
                {'position': 7, 'team': 'Haas', 'points': 34},
                {'position': 8, 'team': 'Aston Martin', 'points': 61},
                {'position': 9, 'team': 'Williams', 'points': 5},
                {'position': 10, 'team': 'Kicksauber', 'points': 1},
            ],
            2021: [
                {'position': 1, 'team': 'Mercedes', 'points': 613},
                {'position': 2, 'team': 'Red Bull Racing', 'points': 468},
                {'position': 3, 'team': 'Ferrari', 'points': 429},
                {'position': 4, 'team': 'McLaren', 'points': 268},
                {'position': 5, 'team': 'Alpine', 'points': 81},
                {'position': 6, 'team': 'Aston Martin', 'points': 15},
                {'position': 7, 'team': 'Williams', 'points': 203},
                {'position': 8, 'team': 'Alfa Romeo', 'points': 13},
                {'position': 9, 'team': 'Haas', 'points': 3},
                {'position': 10, 'team': 'Toro Rosso', 'points': 3},
            ],
            2020: [
                {'position': 1, 'team': 'Mercedes', 'points': 573},
                {'position': 2, 'team': 'Red Bull Racing', 'points': 319},
                {'position': 3, 'team': 'McLaren', 'points': 202},
                {'position': 4, 'team': 'Racing Point', 'points': 195},
                {'position': 5, 'team': 'Ferrari', 'points': 131},
                {'position': 6, 'team': 'AlphaTauri', 'points': 75},
                {'position': 7, 'team': 'Renault', 'points': 119},
                {'position': 8, 'team': 'Williams', 'points': 10},
                {'position': 9, 'team': 'Haas', 'points': 3},
                {'position': 10, 'team': 'Alfa Romeo', 'points': 1},
            ],
            2019: [
                {'position': 1, 'team': 'Mercedes', 'points': 735},
                {'position': 2, 'team': 'Ferrari', 'points': 552},
                {'position': 3, 'team': 'Red Bull Racing', 'points': 417},
                {'position': 4, 'team': 'McLaren', 'points': 145},
                {'position': 5, 'team': 'Renault', 'points': 91},
                {'position': 6, 'team': 'Racing Point', 'points': 57},
                {'position': 7, 'team': 'AlphaTauri', 'points': 85},
                {'position': 8, 'team': 'Alfa Romeo', 'points': 8},
                {'position': 9, 'team': 'Haas', 'points': 28},
                {'position': 10, 'team': 'Williams', 'points': 1},
            ],
            2018: [
                {'position': 1, 'team': 'Mercedes', 'points': 655},
                {'position': 2, 'team': 'Ferrari', 'points': 571},
                {'position': 3, 'team': 'Red Bull Racing', 'points': 427},
                {'position': 4, 'team': 'Haas', 'points': 93},
                {'position': 5, 'team': 'McLaren', 'points': 181},
                {'position': 6, 'team': 'Force India', 'points': 62},
                {'position': 7, 'team': 'Renault', 'points': 53},
                {'position': 8, 'team': 'Toro Rosso', 'points': 51},
                {'position': 9, 'team': 'Williams', 'points': 7},
                {'position': 10, 'team': 'Sauber', 'points': 1},
            ],
            2017: [
                {'position': 1, 'team': 'Mercedes', 'points': 668},
                {'position': 2, 'team': 'Ferrari', 'points': 544},
                {'position': 3, 'team': 'Red Bull Racing', 'points': 368},
                {'position': 4, 'team': 'Force India', 'points': 187},
                {'position': 5, 'team': 'McLaren', 'points': 76},
                {'position': 6, 'team': 'Williams', 'points': 69},
                {'position': 7, 'team': 'Toro Rosso', 'points': 54},
                {'position': 8, 'team': 'Renault', 'points': 39},
                {'position': 9, 'team': 'Sauber', 'points': 20},
                {'position': 10, 'team': 'Haas', 'points': 1},
            ],
            2016: [
                {'position': 1, 'team': 'Mercedes', 'points': 752},
                {'position': 2, 'team': 'Red Bull Racing', 'points': 490},
                {'position': 3, 'team': 'Ferrari', 'points': 398},
                {'position': 4, 'team': 'Force India', 'points': 173},
                {'position': 5, 'team': 'McLaren', 'points': 76},
                {'position': 6, 'team': 'Toro Rosso', 'points': 33},
                {'position': 7, 'team': 'Williams', 'points': 138},
                {'position': 8, 'team': 'Renault', 'points': 16},
                {'position': 9, 'team': 'Sauber', 'points': 2},
                {'position': 10, 'team': 'Haas', 'points': 1},
            ],
            2015: [
                {'position': 1, 'team': 'Mercedes', 'points': 703},
                {'position': 2, 'team': 'Ferrari', 'points': 464},
                {'position': 3, 'team': 'Red Bull Racing', 'points': 240},
                {'position': 4, 'team': 'Williams', 'points': 374},
                {'position': 5, 'team': 'Force India', 'points': 136},
                {'position': 6, 'team': 'Toro Rosso', 'points': 49},
                {'position': 7, 'team': 'McLaren', 'points': 66},
                {'position': 8, 'team': 'Lotus', 'points': 5},
                {'position': 9, 'team': 'Sauber', 'points': 27},
                {'position': 10, 'team': 'Marussia', 'points': 0},
            ],
            2014: [
                {'position': 1, 'team': 'Mercedes', 'points': 701},
                {'position': 2, 'team': 'Red Bull Racing', 'points': 405},
                {'position': 3, 'team': 'Williams', 'points': 256},
                {'position': 4, 'team': 'Ferrari', 'points': 328},
                {'position': 5, 'team': 'McLaren', 'points': 181},
                {'position': 6, 'team': 'Force India', 'points': 78},
                {'position': 7, 'team': 'Toro Rosso', 'points': 22},
                {'position': 8, 'team': 'Lotus', 'points': 33},
                {'position': 9, 'team': 'Sauber', 'points': 16},
                {'position': 10, 'team': 'Marussia', 'points': 0},
            ],
            2010: [
                {'position': 1, 'team': 'Red Bull Racing', 'points': 498},
                {'position': 2, 'team': 'Ferrari', 'points': 395},
                {'position': 3, 'team': 'McLaren', 'points': 454},
                {'position': 4, 'team': 'Mercedes', 'points': 214},
                {'position': 5, 'team': 'Renault', 'points': 136},
                {'position': 6, 'team': 'Williams', 'points': 63},
                {'position': 7, 'team': 'Force India', 'points': 47},
                {'position': 8, 'team': 'Sauber', 'points': 44},
                {'position': 9, 'team': 'Toro Rosso', 'points': 34},
                {'position': 10, 'team': 'Lotus', 'points': 0},
            ],
        }

        count = 0
        for year, standings in constructor_standings.items():
            try:
                season = Season.objects.get(year=year)
                for standing in standings:
                    # Store constructor standings as SeasonResult with driver name as constructor
                    result, created = SeasonResult.objects.get_or_create(
                        season=season,
                        position=standing['position'] + 100,  # Offset to differentiate from driver standings
                        defaults={
                            'driver': standing['team'] + ' (Constructor)',
                            'team': standing['team'],
                            'points': standing['points']
                        }
                    )
                    if created:
                        count += 1
            except Season.DoesNotExist:
                pass
        
        self.stdout.write(self.style.SUCCESS(f'  ✓ Added {count} constructor standings'))

    def add_more_records(self):
        self.stdout.write('\n--- Adding More Records ---')
        new_records = [
            {
                'category': 'driver',
                'title': 'Youngest F1 Driver',
                'value': '17 years 73 days',
                'holder': 'Max Verstappen',
                'year': 2015,
                'description': 'Max Verstappen became the youngest F1 driver ever at Toro Rosso.'
            },
            {
                'category': 'driver',
                'title': 'Most Consecutive Podiums',
                'value': '9 races',
                'holder': 'Mark Webber',
                'year': 2011,
                'description': 'Mark Webber achieved 9 consecutive podium finishes.'
            },
            {
                'category': 'race',
                'title': 'Most Races in a Career',
                'value': '396',
                'holder': 'Fernando Alonso',
                'year': 2024,
                'description': 'Fernando Alonso holds the record for most races competed.'
            },
            {
                'category': 'driver',
                'title': 'Most Wins Without Championship',
                'value': '35',
                'holder': 'Carlos Sainz',
                'year': 2024,
                'description': 'Carlos Sainz has 35 wins but no world championship.'
            },
            {
                'category': 'race',
                'title': 'Most Cars to Finish',
                'value': '20 cars',
                'holder': '2023 Monaco GP',
                'year': 2023,
                'description': 'Maximum number of cars completed the race distance.'
            },
            {
                'category': 'constructor',
                'title': 'Highest Points in a Season',
                'value': '880 points',
                'holder': 'Red Bull Racing',
                'year': 2023,
                'description': 'Red Bull Racing scored 880 points in the 2023 season.'
            },
            {
                'category': 'driver',
                'title': 'Quickest Pit Stop',
                'value': '1.82 seconds',
                'holder': 'Red Bull Racing',
                'year': 2022,
                'description': 'Fastest pit stop ever recorded in Formula 1.'
            },
            {
                'category': 'race',
                'title': 'Most Safety Car Periods',
                'value': '6 periods',
                'holder': '2021 Abu Dhabi GP',
                'year': 2021,
                'description': 'Record number of safety car deployments in a single race.'
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

    def add_more_glossary(self):
        self.stdout.write('\n--- Adding More Glossary Terms ---')
        new_glossary = [
            {
                'term': 'Suspension',
                'definition': 'The system connecting wheels to the chassis, managing ride height and handling.',
                'category': 'Technical'
            },
            {
                'term': 'Steering Ratio',
                'definition': 'The relationship between steering wheel input and front wheel movement.',
                'category': 'Technical'
            },
            {
                'term': 'Camber',
                'definition': 'The angle of the wheels relative to vertical, affecting grip and tire wear.',
                'category': 'Technical'
            },
            {
                'term': 'Toe-in',
                'definition': 'The angle between wheel direction and car centerline, affecting stability.',
                'category': 'Technical'
            },
            {
                'term': 'Anti-roll Bar',
                'definition': 'A suspension component reducing body roll in corners.',
                'category': 'Technical'
            },
            {
                'term': 'Tire Degradation',
                'definition': 'The loss of grip and performance of tires over race distance.',
                'category': 'Technical'
            },
            {
                'term': 'Fuel Strategy',
                'definition': 'The planned fuel consumption and pit stop timing during a race.',
                'category': 'Racing'
            },
            {
                'term': 'Two-stop Strategy',
                'definition': 'Making two pit stops during a race for tire changes.',
                'category': 'Racing'
            },
            {
                'term': 'One-stop Strategy',
                'definition': 'Completing a race with only one pit stop for new tires.',
                'category': 'Racing'
            },
            {
                'term': 'No-stop Strategy',
                'definition': 'Completing the entire race without entering the pit lane.',
                'category': 'Racing'
            },
            {
                'term': 'Turbo',
                'definition': 'A forced induction system increasing engine power output.',
                'category': 'Technical'
            },
            {
                'term': 'MGU-K',
                'definition': 'Motor Generator Unit-Kinetic recovering braking energy.',
                'category': 'Technical'
            },
            {
                'term': 'MGU-H',
                'definition': 'Motor Generator Unit-Heat recovering turbo waste heat.',
                'category': 'Technical'
            },
            {
                'term': 'ERS',
                'definition': 'Energy Recovery System storing and releasing energy during races.',
                'category': 'Technical'
            },
            {
                'term': 'Traction',
                'definition': 'The grip available for acceleration and cornering.',
                'category': 'Racing'
            },
            {
                'term': 'Throttle Control',
                'definition': 'Precise management of accelerator input for smooth power delivery.',
                'category': 'Racing'
            },
            {
                'term': 'Brake Temp',
                'definition': 'The temperature of brake components affecting stopping power.',
                'category': 'Technical'
            },
            {
                'term': 'Tire Pressure',
                'definition': 'Air pressure inside tires affecting grip and handling.',
                'category': 'Technical'
            },
            {
                'term': 'Track Evolution',
                'definition': 'How track grip increases as more cars run on it.',
                'category': 'Racing'
            },
            {
                'term': 'Delta Time',
                'definition': 'The time difference between consecutive lap times or drivers.',
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

    def add_more_tyres(self):
        self.stdout.write('\n--- Adding More Tyre Information ---')
        new_tyres = [
            {
                'name': 'Pirelli P Zero Soft',
                'compound': 'soft',
                'colour': '#FF0000',
                'description': 'Pirelli P Zero Soft compound with highest grip and red sidewalls.',
                'best_used_for': 'Qualifying, street circuits, and short stints',
                'average_stint_length': '15-25 laps'
            },
            {
                'name': 'Pirelli P Zero Medium',
                'compound': 'medium',
                'colour': '#FFFF00',
                'description': 'Pirelli P Zero Medium compound balancing performance and durability.',
                'best_used_for': 'Mixed conditions and flexible strategy',
                'average_stint_length': '20-35 laps'
            },
            {
                'name': 'Pirelli P Zero Hard',
                'compound': 'hard',
                'colour': '#FFFFFF',
                'description': 'Pirelli P Zero Hard compound for maximum durability.',
                'best_used_for': 'Long stints and high-temperature circuits',
                'average_stint_length': '30-50 laps'
            },
            {
                'name': 'Pirelli P Zero Intermediate',
                'compound': 'intermediate',
                'colour': '#00FF00',
                'description': 'Intermediate tires for drying track conditions.',
                'best_used_for': 'Transition between wet and dry conditions',
                'average_stint_length': '10-20 laps'
            },
            {
                'name': 'Pirelli Cinturato Wet',
                'compound': 'wet',
                'colour': '#0000FF',
                'description': 'Cinturato full wet tires for heavy rain.',
                'best_used_for': 'Standing water and heavy precipitation',
                'average_stint_length': '5-15 laps'
            },
        ]

        for tyre_data in new_tyres:
            tyre, created = Tyre.objects.get_or_create(
                name=tyre_data['name'],
                defaults=tyre_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {tyre.name}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {tyre.name}')
