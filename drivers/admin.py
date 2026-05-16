from django.contrib import admin
from .models import Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'driver_number', 'championships', 'wins')
    search_fields = ('name', 'nationality')
    list_filter = ('nationality', 'championships')