from django.contrib import admin
from .models import TerminologyTerm

@admin.register(TerminologyTerm)
class TerminologyAdmin(admin.ModelAdmin):
    list_display = ('term', 'category')
    search_fields = ('term',)
    list_filter = ('category',)