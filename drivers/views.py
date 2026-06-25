from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Driver

def driver_list(request):
    drivers = list(Driver.objects.all())
    print("DRIVERS FOUND:", len(drivers))
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    periods = list(driver.team_periods.all())
    timeline_periods = []
    timeline_start = driver.debut_year
    timeline_end = date.today().year
    if periods:
        timeline_start = periods[0].start_year
        timeline_end = max(p.active_end_year() for p in periods)
        total_years = max(timeline_end - timeline_start + 1, 1)
        for period in periods:
            active_end = period.active_end_year()
            width = round(((active_end - period.start_year + 1) / total_years) * 100, 2)
            timeline_periods.append({
                'team_name': period.team_name,
                'team_color': period.team_color,
                'start_year': period.start_year,
                'end_year': active_end,
                'width': width,
                'label': period.range_label(),
            })
    return render(request, 'drivers/driver_detail.html', {
        'driver': driver,
        'timeline_periods': timeline_periods,
        'timeline_start': timeline_start,
        'timeline_end': timeline_end,
    })