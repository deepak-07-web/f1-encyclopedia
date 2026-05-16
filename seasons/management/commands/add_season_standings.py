from django.core.management.base import BaseCommand
from seasons.models import Season, SeasonResult

class Command(BaseCommand):
    help = 'Add driver standings for all F1 seasons (does NOT delete existing data)'

    def handle(self, *args, **options):
        self.stdout.write('\n--- Adding Driver Standings ---')
        
        self.add_season_standings()
        
        self.stdout.write(self.style.SUCCESS('\n✓ All driver standings added successfully!\n'))

    def add_season_standings(self):
        standings_data = {
            2025: [
                {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 450},
                {'position': 2, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 420},
                {'position': 3, 'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 380},
                {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 370},
                {'position': 5, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 340},
                {'position': 6, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 290},
                {'position': 7, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 280},
                {'position': 8, 'driver': 'Fernando Alonso', 'team': 'Aston Martin', 'points': 220},
                {'position': 9, 'driver': 'Nico Hulkenberg', 'team': 'Haas', 'points': 110},
                {'position': 10, 'driver': 'Pierre Gasly', 'team': 'Alpine', 'points': 85},
            ],
            2023: [
                {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 575},
                {'position': 2, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 438},
                {'position': 3, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 406},
                {'position': 4, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 340},
                {'position': 5, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 308},
                {'position': 6, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 305},
                {'position': 7, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 188},
                {'position': 8, 'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 179},
                {'position': 9, 'driver': 'Fernando Alonso', 'team': 'Aston Martin', 'points': 90},
                {'position': 10, 'driver': 'Yuki Tsunoda', 'team': 'AlphaTauri', 'points': 44},
            ],
            2022: [
                {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 454},
                {'position': 2, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 308},
                {'position': 3, 'driver': 'George Russell', 'team': 'Mercedes', 'points': 308},
                {'position': 4, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 305},
                {'position': 5, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 305},
                {'position': 6, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 240},
                {'position': 7, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 122},
                {'position': 8, 'driver': 'Esteban Ocon', 'team': 'Alpine', 'points': 92},
                {'position': 9, 'driver': 'Fernando Alonso', 'team': 'Alpine', 'points': 81},
                {'position': 10, 'driver': 'Yuki Tsunoda', 'team': 'AlphaTauri', 'points': 46},
            ],
            2021: [
                {'position': 1, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 394},
                {'position': 2, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 387},
                {'position': 3, 'driver': 'Valtteri Bottas', 'team': 'Mercedes', 'points': 226},
                {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 221},
                {'position': 5, 'driver': 'Carlos Sainz', 'team': 'Ferrari', 'points': 208},
                {'position': 6, 'driver': 'George Russell', 'team': 'Williams', 'points': 203},
                {'position': 7, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 153},
                {'position': 8, 'driver': 'Daniel Ricciardo', 'team': 'McLaren', 'points': 115},
                {'position': 9, 'driver': 'Fernando Alonso', 'team': 'Alpine', 'points': 81},
                {'position': 10, 'driver': 'Sergio Perez', 'team': 'Red Bull Racing', 'points': 74},
            ],
            2020: [
                {'position': 1, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 347},
                {'position': 2, 'driver': 'Valtteri Bottas', 'team': 'Mercedes', 'points': 226},
                {'position': 3, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 214},
                {'position': 4, 'driver': 'Alexander Albon', 'team': 'Red Bull Racing', 'points': 105},
                {'position': 5, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 98},
                {'position': 6, 'driver': 'Carlos Sainz', 'team': 'McLaren', 'points': 97},
                {'position': 7, 'driver': 'Daniel Ricciardo', 'team': 'Renault', 'points': 119},
                {'position': 8, 'driver': 'Sergio Perez', 'team': 'Racing Point', 'points': 125},
                {'position': 9, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 114},
                {'position': 10, 'driver': 'Pierre Gasly', 'team': 'AlphaTauri', 'points': 75},
            ],
            2019: [
                {'position': 1, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 413},
                {'position': 2, 'driver': 'Sebastian Vettel', 'team': 'Ferrari', 'points': 288},
                {'position': 3, 'driver': 'Valtteri Bottas', 'team': 'Mercedes', 'points': 322},
                {'position': 4, 'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 264},
                {'position': 5, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 278},
                {'position': 6, 'driver': 'Pierre Gasly', 'team': 'Red Bull Racing', 'points': 95},
                {'position': 7, 'driver': 'Daniel Ricciardo', 'team': 'Renault', 'points': 54},
                {'position': 8, 'driver': 'Sergio Perez', 'team': 'Racing Point', 'points': 57},
                {'position': 9, 'driver': 'Nico Hulkenberg', 'team': 'Renault', 'points': 37},
                {'position': 10, 'driver': 'Lando Norris', 'team': 'McLaren', 'points': 48},
            ],
            2018: [
                {'position': 1, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 408},
                {'position': 2, 'driver': 'Sebastian Vettel', 'team': 'Ferrari', 'points': 320},
                {'position': 3, 'driver': 'Kimi Räikkönen', 'team': 'Ferrari', 'points': 251},
                {'position': 4, 'driver': 'Valtteri Bottas', 'team': 'Mercedes', 'points': 247},
                {'position': 5, 'driver': 'Daniel Ricciardo', 'team': 'Red Bull Racing', 'points': 214},
                {'position': 6, 'driver': 'Sergio Perez', 'team': 'Force India', 'points': 62},
                {'position': 7, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 213},
                {'position': 8, 'driver': 'Kevin Magnussen', 'team': 'Haas', 'points': 56},
                {'position': 9, 'driver': 'Romain Grosjean', 'team': 'Haas', 'points': 42},
                {'position': 10, 'driver': 'Pierre Gasly', 'team': 'Toro Rosso', 'points': 29},
            ],
            2017: [
                {'position': 1, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 363},
                {'position': 2, 'driver': 'Sebastian Vettel', 'team': 'Ferrari', 'points': 320},
                {'position': 3, 'driver': 'Valtteri Bottas', 'team': 'Mercedes', 'points': 305},
                {'position': 4, 'driver': 'Kimi Räikkönen', 'team': 'Ferrari', 'points': 272},
                {'position': 5, 'driver': 'Daniel Ricciardo', 'team': 'Red Bull Racing', 'points': 200},
                {'position': 6, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 168},
                {'position': 7, 'driver': 'Sergio Perez', 'team': 'Force India', 'points': 100},
                {'position': 8, 'driver': 'Esteban Ocon', 'team': 'Force India', 'points': 87},
                {'position': 9, 'driver': 'Carlos Sainz', 'team': 'Toro Rosso', 'points': 54},
                {'position': 10, 'driver': 'Nico Hulkenberg', 'team': 'Renault', 'points': 39},
            ],
            2016: [
                {'position': 1, 'driver': 'Nico Rosberg', 'team': 'Mercedes', 'points': 385},
                {'position': 2, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 367},
                {'position': 3, 'driver': 'Daniel Ricciardo', 'team': 'Red Bull Racing', 'points': 256},
                {'position': 4, 'driver': 'Max Verstappen', 'team': 'Red Bull Racing', 'points': 234},
                {'position': 5, 'driver': 'Sebastian Vettel', 'team': 'Ferrari', 'points': 212},
                {'position': 6, 'driver': 'Kimi Räikkönen', 'team': 'Ferrari', 'points': 186},
                {'position': 7, 'driver': 'Sergio Perez', 'team': 'Force India', 'points': 101},
                {'position': 8, 'driver': 'Jenson Button', 'team': 'McLaren', 'points': 76},
                {'position': 9, 'driver': 'Nico Hulkenberg', 'team': 'Force India', 'points': 72},
                {'position': 10, 'driver': 'Fernando Alonso', 'team': 'McLaren', 'points': 11},
            ],
            2015: [
                {'position': 1, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 381},
                {'position': 2, 'driver': 'Nico Rosberg', 'team': 'Mercedes', 'points': 322},
                {'position': 3, 'driver': 'Sebastian Vettel', 'team': 'Ferrari', 'points': 278},
                {'position': 4, 'driver': 'Kimi Räikkönen', 'team': 'Ferrari', 'points': 186},
                {'position': 5, 'driver': 'Daniel Ricciardo', 'team': 'Red Bull Racing', 'points': 191},
                {'position': 6, 'driver': 'Max Verstappen', 'team': 'Toro Rosso', 'points': 49},
                {'position': 7, 'driver': 'Sergio Perez', 'team': 'Force India', 'points': 78},
                {'position': 8, 'driver': 'Jenson Button', 'team': 'McLaren', 'points': 66},
                {'position': 9, 'driver': 'Felipe Nasr', 'team': 'Sauber', 'points': 27},
                {'position': 10, 'driver': 'Nico Hulkenberg', 'team': 'Force India', 'points': 58},
            ],
            2014: [
                {'position': 1, 'driver': 'Lewis Hamilton', 'team': 'Mercedes', 'points': 384},
                {'position': 2, 'driver': 'Nico Rosberg', 'team': 'Mercedes', 'points': 317},
                {'position': 3, 'driver': 'Daniel Ricciardo', 'team': 'Red Bull Racing', 'points': 238},
                {'position': 4, 'driver': 'Sebastian Vettel', 'team': 'Ferrari', 'points': 167},
                {'position': 5, 'driver': 'Fernando Alonso', 'team': 'Ferrari', 'points': 161},
                {'position': 6, 'driver': 'Valtteri Bottas', 'team': 'Williams', 'points': 122},
                {'position': 7, 'driver': 'Jenson Button', 'team': 'McLaren', 'points': 126},
                {'position': 8, 'driver': 'Felipe Massa', 'team': 'Williams', 'points': 134},
                {'position': 9, 'driver': 'Kevin Magnussen', 'team': 'McLaren', 'points': 55},
                {'position': 10, 'driver': 'Sergio Perez', 'team': 'Force India', 'points': 78},
            ],
            2010: [
                {'position': 1, 'driver': 'Sebastian Vettel', 'team': 'Red Bull Racing', 'points': 256},
                {'position': 2, 'driver': 'Fernando Alonso', 'team': 'Ferrari', 'points': 251},
                {'position': 3, 'driver': 'Felipe Massa', 'team': 'Ferrari', 'points': 144},
                {'position': 4, 'driver': 'Mark Webber', 'team': 'Red Bull Racing', 'points': 242},
                {'position': 5, 'driver': 'Lewis Hamilton', 'team': 'McLaren', 'points': 240},
                {'position': 6, 'driver': 'Jenson Button', 'team': 'McLaren', 'points': 214},
                {'position': 7, 'driver': 'Robert Kubica', 'team': 'Renault', 'points': 136},
                {'position': 8, 'driver': 'Michael Schumacher', 'team': 'Mercedes', 'points': 72},
                {'position': 9, 'driver': 'Rubens Barrichello', 'team': 'Williams', 'points': 63},
                {'position': 10, 'driver': 'Nico Rosberg', 'team': 'Mercedes', 'points': 142},
            ],
        }

        for year, standings in standings_data.items():
            try:
                season = Season.objects.get(year=year)
                for standing in standings:
                    result, created = SeasonResult.objects.get_or_create(
                        season=season,
                        position=standing['position'],
                        defaults={
                            'driver': standing['driver'],
                            'team': standing['team'],
                            'points': standing['points']
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {year} - P{standing["position"]} - {standing["driver"]}'))
                    else:
                        self.stdout.write(f'  ⊘ Exists: {year} - P{standing["position"]} - {standing["driver"]}')
            except Season.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'  ⚠ Season {year} not found'))
