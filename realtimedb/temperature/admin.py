from django.contrib import admin
from .models import Temperature


class TemperatureAdmin(admin.ModelAdmin):
    TIME_FORMAT = '%b %d %Y, %H:%M:%S'

    def created_at_detailed(self, obj):
        return obj.created_at.strftime(self.TIME_FORMAT)
    created_at_detailed.short_description = 'Created At Detailed'

    def updated_at_detailed(self, obj):
        return obj.updated_at.strftime(self.TIME_FORMAT)
    updated_at_detailed.short_description = 'Updated At Detailed'

    list_display = ('id', 'value', 'location', 'created_at_detailed', 'updated_at_detailed')


admin.site.register(Temperature, TemperatureAdmin)
