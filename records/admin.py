from django.contrib import admin
from .models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'holder', 'value')
    search_fields = ('title', 'holder')
    list_filter = ('category',)