from datetime import date

from django import forms

from .models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        instance = Driver
        fields = ['departure', 'arrival', 'departure_date',
                  'departure_time', 'arrival_date', 'arrival_time',
                  'phonenumber']

    def clean_departure(self):
        data = self.cleaned_data
        if not data['departure'][0].isupper():
            raise forms.validators("Departure location"
                                   "should start wtih capital letter")
        if not data['departure'][1:].islower():
            raise forms.ValidationError("The only capital letter should"
                                        "be the first one")

    def clean_arrival(self):
        data = self.cleaned_data
        if not data['arrival'][0].isupper():
            raise forms.ValidationError("Arrival location"
                                        "shold start with a capital letter")
        if not data['departure'][1:].islower():
            raise forms.ValidationError("The only capital letter should"
                                        "be the first one")

    def clean_departure_date(self):
        data = self.cleaned_data
        if data['departure_date'] < date.now():
            raise forms.ValidationError("Enter a valid date")

    def clean_arrival_date(self):
        data = self.cleaned_data
        if data['arrival_date'] < data.now():
            raise forms.ValidationError("Enter a valid date")
        elif data['arrival_date'] < data['departure_date']:
            raise forms.ValidationError("Arrival can't be"
                                        "before departure date")
