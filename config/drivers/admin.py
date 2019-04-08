from django.contrib import admin

from .models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ['author']

admin.site.register(Driver, DriverAdmin)
