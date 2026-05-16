from django.contrib import admin
from .models import Tyre

@admin.register(Tyre)
class TyreAdmin(admin.ModelAdmin):
    list_display = ('name', 'compound', 'colour')
    list_filter = ('compound',)