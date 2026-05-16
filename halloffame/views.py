from django.shortcuts import render
from .models import Legend

def legend_list(request):
    legends = Legend.objects.all()
    return render(request, 'halloffame/legend_list.html', {'legends': legends})