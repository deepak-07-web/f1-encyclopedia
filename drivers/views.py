from django.shortcuts import render, get_object_or_404
from .models import Driver

def driver_list(request):
    drivers = list(Driver.objects.all())
    print("DRIVERS FOUND:", len(drivers))
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})

def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})