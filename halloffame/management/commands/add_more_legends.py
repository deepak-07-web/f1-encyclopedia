from django.core.management.base import BaseCommand
from halloffame.models import Legend

class Command(BaseCommand):
    help = 'Add more legendary F1 drivers to the Hall of Fame'

    def handle(self, *args, **options):
        legends = [
            {
                'name': 'Rene Arnoux',
                'nationality': 'France',
                'era': '1978-1989',
                'championships': 0,
                'wins': 4,
                'bio': 'French driver known for aggressive racing style and memorable battles with Gilles Villeneuve. Competed in 176 Grand Prix races.'
            },
            {
                'name': 'Mario Andretti',
                'nationality': 'United States',
                'era': '1971-1972',
                'championships': 0,
                'wins': 1,
                'bio': 'American legend who competed in F1 briefly but achieved tremendous success in IndyCar racing, winning the Indy 500 and Formula 1 World Drivers Championship equivalent.'
            },
            {
                'name': 'Emerson Fittipaldi',
                'nationality': 'Brazil',
                'era': '1970-1980',
                'championships': 2,
                'wins': 14,
                'bio': 'Brazilian champion who became the youngest World Champion at age 25. Won back-to-back titles in 1972-1973 before becoming a legend in IndyCar.'
            },
            {
                'name': 'Graham Hill',
                'nationality': 'United Kingdom',
                'era': '1958-1975',
                'championships': 2,
                'wins': 14,
                'bio': 'British two-time World Champion and one of only two drivers to win the Monaco Grand Prix five times. Competed in 176 Grand Prix races.'
            },
            {
                'name': 'Damon Hill',
                'nationality': 'United Kingdom',
                'era': '1992-1999',
                'championships': 1,
                'wins': 22,
                'bio': 'Son of Graham Hill, British World Champion in 1996. One of the most successful drivers of the 1990s with a distinguished career spanning 162 races.'
            },
            {
                'name': 'Nelson Piquet',
                'nationality': 'Brazil',
                'era': '1978-1991',
                'championships': 3,
                'wins': 23,
                'bio': 'Brazilian three-time World Champion who dominated F1 in the 1980s. Known for aggressive driving and political acumen, competed in 204 Grand Prix races.'
            },
            {
                'name': 'Kimi Räikkönen',
                'nationality': 'Finland',
                'era': '2001-2021',
                'championships': 1,
                'wins': 21,
                'bio': 'Finnish World Champion in 2007 with Ferrari. Known for his reserved personality and impressive racecraft, accumulated 346 career Grand Prix starts.'
            },
            {
                'name': 'Fernando Alonso',
                'nationality': 'Spain',
                'era': '2001-2023',
                'championships': 2,
                'wins': 32,
                'bio': 'Spanish two-time World Champion. Youngest driver to score points, win, and lead races. Competed in 396 Grand Prix races, the most in F1 history.'
            },
            {
                'name': 'Sebastian Vettel',
                'nationality': 'Germany',
                'era': '2007-2022',
                'championships': 4,
                'wins': 53,
                'bio': 'German four-time World Champion with Red Bull Racing and Ferrari. Known for consistent performance and sportsmanship throughout a 300+ race career.'
            },
            {
                'name': 'Mika Häkkinen',
                'nationality': 'Finland',
                'era': '1991-2001',
                'championships': 2,
                'wins': 20,
                'bio': 'Finnish two-time World Champion who dominated with McLaren in 1998-1999. Known for speed and mental toughness during competitive Mercedes period.'
            },
            {
                'name': 'David Coulthard',
                'nationality': 'United Kingdom',
                'era': '1994-2008',
                'championships': 0,
                'wins': 13,
                'bio': 'British driver with 247 Grand Prix entries. Fought in two World Championships (1997, 1998) and won 13 races with McLaren, Williams, and Red Bull.'
            },
            {
                'name': 'Giancarlo Fisichella',
                'nationality': 'Brazil',
                'era': '1996-2009',
                'championships': 0,
                'wins': 3,
                'bio': 'Brazilian driver and Ferrari number two during Michael Schumacher era (2003-2009). Competed in 308 Grand Prix races with Ferrari and Renault.'
            },
            {
                'name': 'Juan Pablo Montoya',
                'nationality': 'Colombia',
                'era': '2001-2006',
                'championships': 0,
                'wins': 16,
                'bio': 'Colombian driver known for aggressive overtaking and competitive spirit. Won 16 races in 223 Grand Prix starts with Williams and McLaren.'
            },
            {
                'name': 'Felipe Massa',
                'nationality': 'Brazil',
                'era': '2002-2017',
                'championships': 0,
                'wins': 11,
                'bio': 'Brazilian driver who came close to World Championship in 2008. Competed in 272 races with Ferrari, Williams, and other teams.'
            },
            {
                'name': 'Mark Webber',
                'nationality': 'Australia',
                'era': '2002-2013',
                'championships': 0,
                'wins': 9,
                'bio': 'Australian driver who achieved 122 podiums in 308 races. Strong performer with Red Bull Racing alongside Sebastian Vettel.'
            },
            {
                'name': 'Rubens Barrichello',
                'nationality': 'Brazil',
                'era': '1992-2012',
                'championships': 0,
                'wins': 11,
                'bio': 'Brazilian driver with most Grand Prix starts (326) for many years. Loyal Ferrari teammate during Schumacher era and successful throughout his career.'
            },
            {
                'name': 'Gerhard Berger',
                'nationality': 'Austria',
                'era': '1984-1997',
                'championships': 0,
                'wins': 10,
                'bio': 'Austrian driver known for competitive spirit and longevity. Won 10 races across 210 Grand Prix starts with Ferrari, Benetton, and McLaren.'
            },
            {
                'name': 'Thierry Boutsen',
                'nationality': 'Belgium',
                'era': '1983-1993',
                'championships': 0,
                'wins': 3,
                'bio': 'Belgian driver who competed in 163 Grand Prix races. Won races with Ferrari and Williams during the 1980s and 1990s.'
            },
            {
                'name': 'Mauricio Gugelmin',
                'nationality': 'Brazil',
                'era': '1988-1992',
                'championships': 0,
                'wins': 0,
                'bio': 'Brazilian driver who competed in 76 Grand Prix races. Built valuable experience with March, Leyton House, and Arrows teams.'
            },
            {
                'name': 'Martin Donnelly',
                'nationality': 'United Kingdom',
                'era': '1989-1990',
                'championships': 0,
                'wins': 0,
                'bio': 'British driver who survived a major crash at Jerez. Despite limited F1 career with 31 races, became a noted sports commentator.'
            },
            {
                'name': 'Derek Warwick',
                'nationality': 'United Kingdom',
                'era': '1981-1989',
                'championships': 0,
                'wins': 0,
                'bio': 'British driver who competed in 147 Grand Prix races. Strong performer who came close to podiums but never achieved victory in F1.'
            },
            {
                'name': 'Stefan Johansson',
                'nationality': 'Sweden',
                'era': '1983-1991',
                'championships': 0,
                'wins': 0,
                'bio': 'Swedish driver with 79 Grand Prix entries. Competed during the turbo era with Ferrari, Ligier, and McLaren teams.'
            },
            {
                'name': 'Teo Fabi',
                'nationality': 'Italy',
                'era': '1982-1992',
                'championships': 0,
                'wins': 1,
                'bio': 'Italian driver who scored his only Grand Prix victory in 1983. Competed in 208 races with Toleman, Benetton, and Minardi teams.'
            },
            {
                'name': 'Roberto Guerrero',
                'nationality': 'Colombia',
                'era': '1982-1992',
                'championships': 0,
                'wins': 0,
                'bio': 'Colombian driver with 31 Grand Prix entries. Known for success in American racing series before and after his F1 involvement.'
            },
            {
                'name': 'Riccardo Patrese',
                'nationality': 'Italy',
                'era': '1982-1994',
                'championships': 0,
                'wins': 6,
                'bio': 'Italian driver who holds record for most Grand Prix starts (256). Consistent performer who won 6 races with various teams over his long career.'
            },
        ]

        created_count = 0
        for legend_data in legends:
            legend, created = Legend.objects.get_or_create(
                name=legend_data['name'],
                defaults={
                    'nationality': legend_data['nationality'],
                    'era': legend_data['era'],
                    'championships': legend_data['championships'],
                    'wins': legend_data['wins'],
                    'bio': legend_data['bio'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"  ✓ Added: {legend.name}"))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f"  ✗ Already exists: {legend.name}"))

        self.stdout.write(self.style.SUCCESS(f"\n✓✓✓ Added {created_count} new Hall of Fame legends! ✓✓✓"))
