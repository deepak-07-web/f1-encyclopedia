from django.shortcuts import render, get_object_or_404
from .models import Season, SeasonResult

def season_list(request):
    seasons = Season.objects.all().order_by('-year')
    return render(request, 'seasons/season_list.html', {'seasons': seasons})

def season_detail(request, pk):
    season = get_object_or_404(Season, pk=pk)
    results = SeasonResult.objects.filter(season=season).order_by('position')
    return render(request, 'seasons/season_detail.html', {
        'season': season,
        'results': results,
    })