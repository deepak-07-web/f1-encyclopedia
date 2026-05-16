from django.contrib import admin
from .models import GlossaryTerm

@admin.register(GlossaryTerm)
class GlossaryAdmin(admin.ModelAdmin):
    list_display = ('term', 'category')
    search_fields = ('term',)
    list_filter = ('category',)