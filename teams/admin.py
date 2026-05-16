from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'base', 'founded', 'championships', 'engine_supplier')
    search_fields = ('name', 'base')
    list_filter = ('engine_supplier', 'championships')