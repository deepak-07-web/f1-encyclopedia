#!/usr/bin/env python
"""
Safe data verification script - READ ONLY, NO MODIFICATIONS
Checks data integrity and accuracy without touching database
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'f1_site.settings')
django.setup()

from drivers.models import Driver
from teams.models import Team
from circuits.models import Circuit
from seasons.models import Season, SeasonResult
from records.models import Record
from glossary.models import GlossaryTerm
from halloffame.models import Legend
from tyres.models import Tyre

def verify_drivers():
    print("\n" + "="*60)
    print("DRIVERS VERIFICATION")
    print("="*60)
    drivers = Driver.objects.all()
    print(f"Total Drivers: {drivers.count()}")
    
    for driver in drivers.order_by('name'):
        print(f"\n  • {driver.name} (#{driver.driver_number})")
        print(f"    Nationality: {driver.nationality}")
        print(f"    DOB: {driver.date_of_birth}")
        print(f"    Debut Year: {driver.debut_year}")
        print(f"    Stats: {driver.races} races, {driver.wins} wins, {driver.podiums} podiums, {driver.championships} championships")
        print(f"    Images: main={bool(driver.image)}, helmet={bool(driver.helmet_image)}, action={bool(driver.action_image)}, podium={bool(driver.podium_image)}, young={bool(driver.young_career_image)}, car={bool(driver.car_image)}")

def verify_teams():
    print("\n" + "="*60)
    print("TEAMS VERIFICATION")
    print("="*60)
    teams = Team.objects.all()
    print(f"Total Teams: {teams.count()}")
    
    for team in teams.order_by('name'):
        print(f"\n  • {team.name} ({team.full_name})")
        print(f"    Base: {team.base}")
        print(f"    Founded: {team.founded}")
        print(f"    Team Principal: {team.team_principal}")
        print(f"    Engine: {team.engine_supplier}")
        print(f"    Championships: {team.championships}")
        print(f"    Color: {team.team_color}")
        print(f"    Images: logo={bool(team.logo)}, car={bool(team.car_image)}, garage={bool(team.garage_image)}, podium={bool(team.podium_image)}")

def verify_circuits():
    print("\n" + "="*60)
    print("CIRCUITS VERIFICATION")
    print("="*60)
    circuits = Circuit.objects.all()
    print(f"Total Circuits: {circuits.count()}")
    
    for circuit in circuits.order_by('name'):
        print(f"\n  • {circuit.name} ({circuit.country})")
        print(f"    City: {circuit.city}")
        print(f"    Length: {circuit.length_km}km, Turns: {circuit.turns}, DRS Zones: {circuit.drs_zones}")
        print(f"    First GP: {circuit.first_gp_year}")
        print(f"    Lap Record: {circuit.lap_record_time} by {circuit.lap_record_holder} ({circuit.lap_record_year})")
        print(f"    Images: track={bool(circuit.track_image)}, aerial={bool(circuit.aerial_image)}, corner={bool(circuit.corner_image)}")

def verify_seasons():
    print("\n" + "="*60)
    print("SEASONS VERIFICATION")
    print("="*60)
    seasons = Season.objects.all()
    print(f"Total Seasons: {seasons.count()}")
    
    for season in seasons.order_by('year'):
        print(f"\n  • {season.year}")
        print(f"    Total Races: {season.total_races}")
        print(f"    Champion: {season.drivers_champion}")
        print(f"    Constructor Champion: {season.constructors_champion}")
        print(f"    Driver Standings Records: {SeasonResult.objects.filter(season=season, position__lt=100).count()}")
        print(f"    Constructor Standings Records: {SeasonResult.objects.filter(season=season, position__gte=100).count()}")

def verify_records():
    print("\n" + "="*60)
    print("RECORDS VERIFICATION")
    print("="*60)
    records = Record.objects.all()
    print(f"Total Records: {records.count()}")
    
    for record in records.order_by('title'):
        print(f"\n  • {record.title}")
        print(f"    Holder: {record.holder}")
        print(f"    Value: {record.value}")
        print(f"    Year: {record.year}")

def verify_glossary():
    print("\n" + "="*60)
    print("GLOSSARY VERIFICATION")
    print("="*60)
    terms = GlossaryTerm.objects.all()
    print(f"Total Glossary Terms: {terms.count()}")
    
    for term in terms.order_by('term'):
        print(f"\n  • {term.term}")
        print(f"    Definition (first 80 chars): {term.definition[:80]}...")

def verify_hall_of_fame():
    print("\n" + "="*60)
    print("HALL OF FAME VERIFICATION")
    print("="*60)
    legends = Legend.objects.all()
    print(f"Total Hall of Fame Entries: {legends.count()}")
    
    for legend in legends.order_by('name'):
        print(f"\n  • {legend.name}")
        print(f"    Nationality: {legend.nationality}")
        print(f"    Era: {legend.era}")
        print(f"    Championships: {legend.championships}")
        print(f"    Wins: {legend.wins}")
        print(f"    Image: {bool(legend.image)}")

def verify_tyres():
    print("\n" + "="*60)
    print("TYRES VERIFICATION")
    print("="*60)
    tyres = Tyre.objects.all()
    print(f"Total Tyre Types: {tyres.count()}")
    
    for tyre in tyres.order_by('name'):
        print(f"\n  • {tyre.name}")
        print(f"    Compound: {tyre.compound}")
        print(f"    Color: {tyre.colour}")
        print(f"    Average Stint Length: {tyre.average_stint_length}")
        print(f"    Best Used For: {tyre.best_used_for[:60]}...")
        print(f"    Image: {bool(tyre.image)}")

if __name__ == '__main__':
    print("\n\n🔍 F1 ENCYCLOPEDIA DATA VERIFICATION (READ-ONLY)\n")
    
    verify_drivers()
    verify_teams()
    verify_circuits()
    verify_seasons()
    verify_records()
    verify_glossary()
    verify_hall_of_fame()
    verify_tyres()
    
    print("\n" + "="*60)
    print("✓ VERIFICATION COMPLETE - NO CHANGES MADE")
    print("="*60 + "\n")
