from django.contrib import admin

from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = ['author']

admin.site.register(Package, PackageAdmin)
