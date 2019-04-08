from datetime import date

from django import forms

from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package_width',
                  'package_height', 'package_thickness', 'package_weight',
                  'price', 'phonenumber']


class EditPackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['package_width',
                  'package_height', 'package_thickness', 'package_weight',
                  'price', 'phonenumber']
