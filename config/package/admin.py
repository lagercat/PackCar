from django.contrib import admin

from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = ['author']
    ordering = ['departure_date']

admin.site.register(Package, PackageAdmin)
