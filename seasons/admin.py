from django.contrib import admin
from .models import Season, SeasonResult

class SeasonResultInline(admin.TabularInline):
    model = SeasonResult
    extra = 5

@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('year', 'drivers_champion', 'constructors_champion', 'total_races')
    search_fields = ('year', 'drivers_champion')
    inlines = [SeasonResultInline]