from django.contrib import admin
from .models import Patent

@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patent_date', 'short_patent_data')
    search_fields = ('patent_data',)
    list_filter = ('patent_date',)

    def short_patent_data(self, obj):
        return (obj.patent_data[:50] + '...') if len(obj.patent_data) > 50 else obj.patent_data
    short_patent_data.short_description = 'Patent Data'
