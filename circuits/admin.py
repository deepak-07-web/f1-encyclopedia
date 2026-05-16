from django.contrib import admin
from .models import Circuit

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'length_km', 'first_gp_year')
    search_fields = ('name', 'country')
    list_filter = ('country',)