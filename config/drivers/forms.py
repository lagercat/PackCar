from django import forms

from .models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        instance = Driver
        fields = ['departure', 'arrival', 'departure_date',
                  'departure_time', 'arrival_date', 'arrival_time',
                  'phonenumber']
