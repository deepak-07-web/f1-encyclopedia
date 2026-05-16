from django.shortcuts import render
from .models import Record

def record_list(request):
    driver_records = Record.objects.filter(category='driver')
    constructor_records = Record.objects.filter(category='constructor')
    race_records = Record.objects.filter(category='race')
    return render(request, 'records/record_list.html', {
        'driver_records': driver_records,
        'constructor_records': constructor_records,
        'race_records': race_records,
    })