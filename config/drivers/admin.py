from django.contrib import admin

from .models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ['author']
    ordering = ['departure_date']

admin.site.register(Driver, DriverAdmin)
