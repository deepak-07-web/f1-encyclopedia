from django.contrib import admin
from .models import Legend

@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality', 'championships', 'wins')
    search_fields = ('name',)