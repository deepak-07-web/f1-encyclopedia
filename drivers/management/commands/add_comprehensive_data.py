from django.core.management.base import BaseCommand
from drivers.models import Driver
from teams.models import Team
from seasons.models import Season, SeasonResult
from records.models import Record
from glossary.models import GlossaryTerm
from halloffame.models import Legend
from datetime import date

class Command(BaseCommand):
    help = 'Add comprehensive F1 data: teams, drivers, seasons, records, legends (does NOT delete existing data)'

    def handle(self, *args, **options):
        self.add_teams()
        self.add_more_drivers()
        self.add_more_seasons()
        self.add_more_records()
        self.add_more_glossary()
        self.add_more_legends()
        
        self.stdout.write(self.style.SUCCESS('\n✓✓✓ All comprehensive F1 data added successfully! ✓✓✓\n'))

    def add_teams(self):
        self.stdout.write('\n--- Adding Teams ---')
        new_teams = [
            {
                'name': 'Lotus',
                'full_name': 'Lotus F1 Team',
                'base': 'Enstone, UK',
                'founded': 1958,
                'team_principal': 'Alan Permane',
                'engine_supplier': 'Renault',
                'championships': 2,
                'team_color': '#FFB800',
                'bio': 'Lotus is a historic team with legendary roots and multiple championships in F1 history.'
            },
            {
                'name': 'Brabham',
                'full_name': 'Brabham Racing Organisation',
                'base': 'Chessington, UK',
                'founded': 1962,
                'team_principal': 'Bernie Ecclestone',
                'engine_supplier': 'Repco',
                'championships': 3,
                'team_color': '#1E3050',
                'bio': 'Brabham is a legendary team with three world championships and innovative designs.'
            },
            {
                'name': 'Ligier',
                'full_name': 'Ligier F1 Team',
                'base': 'Maggotts, UK',
                'founded': 1976,
                'team_principal': 'Guy Ligier',
                'engine_supplier': 'Matra',
                'championships': 0,
                'team_color': '#0082FA',
                'bio': 'Ligier was a competitive team known for innovative designs and strong performances.'
            },
            {
                'name': 'Tyrrell',
                'full_name': 'Tyrrell Racing Organisation',
                'base': 'Ockham, UK',
                'founded': 1966,
                'team_principal': 'Ken Tyrrell',
                'engine_supplier': 'Ford',
                'championships': 1,
                'team_color': '#0082FA',
                'bio': 'Tyrrell was a legendary team founded by Ken Tyrrell, famous for innovation and success.'
            },
            {
                'name': 'Benetton',
                'full_name': 'Benetton Formula',
                'base': 'Enstone, UK',
                'founded': 1983,
                'team_principal': 'Flavio Briatore',
                'engine_supplier': 'Ford',
                'championships': 1,
                'team_color': '#1E3050',
                'bio': 'Benetton was a successful team with multiple championships and competitive performances.'
            },
            {
                'name': 'Arrows',
                'full_name': 'Arrows Grand Prix Racing',
                'base': 'Milton Keynes, UK',
                'founded': 1997,
                'team_principal': 'Tom Walkinshaw',
                'engine_supplier': 'Hart',
                'championships': 0,
                'team_color': '#FF0000',
                'bio': 'Arrows was a competitive team that challenged for points in multiple seasons.'
            },
            {
                'name': 'Stewart',
                'full_name': 'Stewart Grand Prix',
                'base': 'Milton Keynes, UK',
                'founded': 1997,
                'team_principal': 'Jackie Stewart',
                'engine_supplier': 'Ford',
                'championships': 0,
                'team_color': '#0082FA',
                'bio': 'Stewart F1 was founded by legendary driver Jackie Stewart and competed successfully.'
            },
            {
                'name': 'Jordan',
                'full_name': 'Jordan Grand Prix',
                'base': 'Silverstone, UK',
                'founded': 1991,
                'team_principal': 'Eddie Jordan',
                'engine_supplier': 'Ford',
                'championships': 0,
                'team_color': '#FFB800',
                'bio': 'Jordan was a competitive Irish team known for discovering young talent and strong performances.'
            },
            {
                'name': 'Minardi',
                'full_name': 'Minardi Team',
                'base': 'Faenza, Italy',
                'founded': 1985,
                'team_principal': 'Paul Stoddart',
                'engine_supplier': 'Ford',
                'championships': 0,
                'team_color': '#1E3050',
                'bio': 'Minardi was the longest-surviving independent team with consistent efforts and development.'
            },
            {
                'name': 'Super Aguri',
                'full_name': 'Super Aguri F1 Team',
                'base': 'Leafield, UK',
                'founded': 2006,
                'team_principal': 'Aguri Suzuki',
                'engine_supplier': 'Honda',
                'championships': 0,
                'team_color': '#1E3050',
                'bio': 'Super Aguri was a Japanese team that competed briefly in Formula 1.'
            },
        ]

        for team_data in new_teams:
            team, created = Team.objects.get_or_create(
                name=team_data['name'],
                defaults=team_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {team.name}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {team.name}')

    def add_more_drivers(self):
        self.stdout.write('\n--- Adding More Drivers ---')
        new_drivers = [
            {
                'name': 'Niki Lauda',
                'nationality': 'Austria',
                'date_of_birth': date(1949, 2, 22),
                'driver_number': 11,
                'abbreviation': 'LAU',
                'races': 177,
                'wins': 25,
                'podiums': 54,
                'pole_positions': 24,
                'fastest_laps': 24,
                'championships': 3,
                'bio': 'Niki Lauda is an Austrian legend with three world championships and incredible racing spirit.',
                'debut_year': 1971
            },
            {
                'name': 'Jackie Stewart',
                'nationality': 'Scotland',
                'date_of_birth': date(1939, 6, 11),
                'driver_number': 1,
                'abbreviation': 'STW',
                'races': 99,
                'wins': 27,
                'podiums': 43,
                'pole_positions': 17,
                'fastest_laps': 15,
                'championships': 3,
                'bio': 'Jackie Stewart is a Scottish legend with three world championships and safety advocacy.',
                'debut_year': 1965
            },
            {
                'name': 'Emerson Fittipaldi',
                'nationality': 'Brazil',
                'date_of_birth': date(1946, 12, 12),
                'driver_number': 72,
                'abbreviation': 'FIT',
                'races': 144,
                'wins': 14,
                'podiums': 35,
                'pole_positions': 7,
                'fastest_laps': 6,
                'championships': 2,
                'bio': 'Emerson Fittipaldi is a Brazilian pioneer with two world championships.',
                'debut_year': 1970
            },
            {
                'name': 'Nigel Mansell',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1953, 8, 8),
                'driver_number': 5,
                'abbreviation': 'MAN',
                'races': 187,
                'wins': 31,
                'podiums': 60,
                'pole_positions': 32,
                'fastest_laps': 30,
                'championships': 1,
                'bio': 'Nigel Mansell is a British driver known for aggressive racing and one world championship.',
                'debut_year': 1980
            },
            {
                'name': 'Damon Hill',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1960, 9, 17),
                'driver_number': 0,
                'abbreviation': 'HIL',
                'races': 162,
                'wins': 22,
                'podiums': 42,
                'pole_positions': 20,
                'fastest_laps': 19,
                'championships': 1,
                'bio': 'Damon Hill is a son of Graham Hill with one world championship and strong performances.',
                'debut_year': 1992
            },
            {
                'name': 'Graham Hill',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1929, 2, 15),
                'driver_number': 1,
                'abbreviation': 'GHI',
                'races': 176,
                'wins': 14,
                'podiums': 36,
                'pole_positions': 13,
                'fastest_laps': 10,
                'championships': 2,
                'bio': 'Graham Hill is a British legend with two world championships and 176 races.',
                'debut_year': 1958
            },
            {
                'name': 'Stirling Moss',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1929, 9, 17),
                'driver_number': 7,
                'abbreviation': 'MOS',
                'races': 66,
                'wins': 16,
                'podiums': 40,
                'pole_positions': 16,
                'fastest_laps': 19,
                'championships': 0,
                'bio': 'Stirling Moss is a legendary driver considered one of the greatest without a world title.',
                'debut_year': 1951
            },
            {
                'name': 'James Hunt',
                'nationality': 'United Kingdom',
                'date_of_birth': date(1947, 8, 29),
                'driver_number': 11,
                'abbreviation': 'HUN',
                'races': 92,
                'wins': 10,
                'podiums': 26,
                'pole_positions': 14,
                'fastest_laps': 5,
                'championships': 1,
                'bio': 'James Hunt is a British champion known for aggressive driving and one world championship.',
                'debut_year': 1973
            },
            {
                'name': 'Ronnie Peterson',
                'nationality': 'Sweden',
                'date_of_birth': date(1944, 2, 14),
                'driver_number': 2,
                'abbreviation': 'PET',
                'races': 123,
                'wins': 10,
                'podiums': 33,
                'pole_positions': 33,
                'fastest_laps': 9,
                'championships': 0,
                'bio': 'Ronnie Peterson was a Swedish driver with impressive pole position records.',
                'debut_year': 1970
            },
            {
                'name': 'Andrea de Cesaris',
                'nationality': 'Italy',
                'date_of_birth': date(1959, 5, 31),
                'driver_number': 9,
                'abbreviation': 'DEC',
                'races': 208,
                'wins': 0,
                'podiums': 4,
                'pole_positions': 0,
                'fastest_laps': 1,
                'championships': 0,
                'bio': 'Andrea de Cesaris had a long F1 career with multiple seasons of competition.',
                'debut_year': 1980
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

    def add_more_seasons(self):
        self.stdout.write('\n--- Adding More Seasons ---')
        new_seasons = [
            {
                'year': 2018,
                'drivers_champion': 'Lewis Hamilton',
                'constructors_champion': 'Mercedes',
                'total_races': 21,
                'description': '2018 season featuring competitive battles between Mercedes and Ferrari.'
            },
            {
                'year': 2017,
                'drivers_champion': 'Lewis Hamilton',
                'constructors_champion': 'Mercedes',
                'total_races': 20,
                'description': '2017 season with new technical regulations and competitive racing.'
            },
            {
                'year': 2016,
                'drivers_champion': 'Nico Rosberg',
                'constructors_champion': 'Mercedes',
                'total_races': 21,
                'description': '2016 season featuring championship battle between Mercedes teammates.'
            },
            {
                'year': 2015,
                'drivers_champion': 'Lewis Hamilton',
                'constructors_champion': 'Mercedes',
                'total_races': 19,
                'description': '2015 season dominated by Mercedes with hybrid power units.'
            },
            {
                'year': 2014,
                'drivers_champion': 'Lewis Hamilton',
                'constructors_champion': 'Mercedes',
                'total_races': 19,
                'description': '2014 marked the start of the hybrid turbo era in Formula 1.'
            },
            {
                'year': 2010,
                'drivers_champion': 'Sebastian Vettel',
                'constructors_champion': 'Red Bull Racing',
                'total_races': 19,
                'description': '2010 season saw Red Bull\'s first championship win with young Vettel.'
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

    def add_more_records(self):
        self.stdout.write('\n--- Adding More Records ---')
        new_records = [
            {
                'category': 'driver',
                'title': 'Most Races Competed',
                'value': '396',
                'holder': 'Fernando Alonso',
                'year': 2024,
                'description': 'Fernando Alonso holds the record for most F1 races competed.'
            },
            {
                'category': 'driver',
                'title': 'Oldest Driver to Score Points',
                'value': '42 years',
                'holder': 'Giancarlo Fisichella',
                'year': 2014,
                'description': 'Giancarlo Fisichella scored points at age 42 in Formula 1.'
            },
            {
                'category': 'constructor',
                'title': 'Most Wins in a Season',
                'value': '21 wins',
                'holder': 'Mercedes',
                'year': 2020,
                'description': 'Mercedes achieved 21 wins in a single 2020 season.'
            },
            {
                'category': 'race',
                'title': 'Fastest Lap Record',
                'value': '1:15.584',
                'holder': 'Max Verstappen',
                'year': 2023,
                'description': 'Max Verstappen set the overall fastest lap on F1 circuits.'
            },
            {
                'category': 'driver',
                'title': 'First Female F1 Driver',
                'value': '1976',
                'holder': 'Maria Teresa de Filippis',
                'year': 1958,
                'description': 'Maria Teresa de Filippis was one of the first female drivers in Formula 1.'
            },
            {
                'category': 'race',
                'title': 'Highest Grid Position Recovered to Win',
                'value': '14th to 1st',
                'holder': 'Ayrton Senna',
                'year': 1985,
                'description': 'Ayrton Senna achieved an incredible comeback win from grid position.'
            },
            {
                'category': 'constructor',
                'title': 'Most Points in a Season',
                'value': '740 points',
                'holder': 'Mercedes',
                'year': 2019,
                'description': 'Mercedes scored a record 740 points in the 2019 season.'
            },
            {
                'category': 'driver',
                'title': 'Most DNFs (Did Not Finish)',
                'value': '117',
                'holder': 'Andrea de Cesaris',
                'year': 1994,
                'description': 'Andrea de Cesaris retired from numerous races during his career.'
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
                'term': 'Aerodynamics',
                'definition': 'The study of air flow around the car to generate downforce and minimize drag.',
                'category': 'Technical'
            },
            {
                'term': 'Ballast',
                'definition': 'Extra weight added to the car to meet minimum weight requirements.',
                'category': 'Technical'
            },
            {
                'term': 'Blistering',
                'definition': 'Small bubbles forming on tire surfaces due to excessive heat and wear.',
                'category': 'Technical'
            },
            {
                'term': 'Cockpit',
                'definition': 'The driver\'s compartment in the car where all controls and displays are located.',
                'category': 'Technical'
            },
            {
                'term': 'Differential',
                'definition': 'The mechanism allowing different wheel speeds in corners.',
                'category': 'Technical'
            },
            {
                'term': 'Downshift',
                'definition': 'Changing to a lower gear for increased engine braking or acceleration.',
                'category': 'Racing'
            },
            {
                'term': 'Engine Mapping',
                'definition': 'Software settings controlling engine performance parameters.',
                'category': 'Technical'
            },
            {
                'term': 'Flag Signals',
                'definition': 'Color-coded flags used to communicate conditions to drivers during races.',
                'category': 'Racing'
            },
            {
                'term': 'Graining',
                'definition': 'Loss of rubber particles from tire surface due to sliding or cold tires.',
                'category': 'Technical'
            },
            {
                'term': 'Hydration',
                'definition': 'The grooves in wet tires that displace water for better traction.',
                'category': 'Technical'
            },
            {
                'term': 'Kerb',
                'definition': 'The curbing at track edges that drivers can use or must avoid.',
                'category': 'Racing'
            },
            {
                'term': 'Lockup',
                'definition': 'When wheels stop rotating during braking, skidding across the track.',
                'category': 'Technical'
            },
            {
                'term': 'Marshalls',
                'definition': 'Track officials managing safety and race procedures on the circuit.',
                'category': 'Racing'
            },
            {
                'term': 'NGT (Next Generation Technology)',
                'definition': 'Modern F1 technologies and innovations in power units and aerodynamics.',
                'category': 'Technical'
            },
            {
                'term': 'Pace Notes',
                'definition': 'Information relayed by pit crew to drivers about track conditions and strategy.',
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

    def add_more_legends(self):
        self.stdout.write('\n--- Adding More Hall of Fame Legends ---')
        new_legends = [
            {
                'name': 'Niki Lauda',
                'nationality': 'Austria',
                'era': '1971-1985',
                'championships': 3,
                'wins': 25,
                'bio': 'Niki Lauda is an Austrian legend with incredible determination and three world championships.'
            },
            {
                'name': 'Jackie Stewart',
                'nationality': 'Scotland',
                'era': '1965-1973',
                'championships': 3,
                'wins': 27,
                'bio': 'Jackie Stewart is a Scottish legend who revolutionized safety in Formula 1.'
            },
            {
                'name': 'Nigel Mansell',
                'nationality': 'United Kingdom',
                'era': '1980-1994',
                'championships': 1,
                'wins': 31,
                'bio': 'Nigel Mansell is a British driver known for aggressive racing and 31 wins.'
            },
            {
                'name': 'Stirling Moss',
                'nationality': 'United Kingdom',
                'era': '1951-1962',
                'championships': 0,
                'wins': 16,
                'bio': 'Stirling Moss is considered one of the greatest drivers despite never winning a championship.'
            },
            {
                'name': 'James Hunt',
                'nationality': 'United Kingdom',
                'era': '1973-1979',
                'championships': 1,
                'wins': 10,
                'bio': 'James Hunt was a flamboyant British champion with exciting driving style.'
            },
        ]

        for legend_data in new_legends:
            legend, created = Legend.objects.get_or_create(
                name=legend_data['name'],
                defaults=legend_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Added: {legend.name}'))
            else:
                self.stdout.write(f'  ⊘ Exists: {legend.name}')
