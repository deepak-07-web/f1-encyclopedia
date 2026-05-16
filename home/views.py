from django.shortcuts import render
from drivers.models import Driver
from teams.models import Team

def homepage(request):
    drivers = Driver.objects.all()[:6]
    teams = Team.objects.all()[:6]
    return render(request, 'home/homepage.html', {
        'drivers': drivers,
        'teams': teams,
    })