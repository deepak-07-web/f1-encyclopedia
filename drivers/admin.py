from django.contrib import admin
from .models import Driver, DriverTeamPeriod


class DriverTeamPeriodInline(admin.TabularInline):
    model = DriverTeamPeriod
    extra = 1
    fields = ('team_name', 'team_color', 'start_year', 'end_year', 'order')
    ordering = ('start_year', 'order')


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    inlines = [DriverTeamPeriodInline]
    list_display = ('name', 'team_name', 'nationality', 'driver_number', 'championships', 'wins')
    search_fields = ('name', 'nationality', 'team_name')
    list_filter = ('nationality', 'championships')