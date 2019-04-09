from django.contrib import admin

from .models import Package, Offer


class PackageAdmin(admin.ModelAdmin):
    list_display = ['author']
    

class OfferAdmin(admin.ModelAdmin):
    list_display = ['accepted']


admin.site.register(Package, PackageAdmin)
admin.site.register(Offer, OfferAdmin)

