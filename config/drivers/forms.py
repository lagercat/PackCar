from datetime import date

from django import forms

from .models import Driver


class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ['departure', 'arrival', 'departure_date',
                  'departure_time', 'arrival_date', 'arrival_time',
                  'phonenumber']

    def clean_departure(self):
        data = self.cleaned_data
        if not data['departure'][0].isupper():
            raise forms.ValidationError("Departure location"
                                        " should start wtih capital letter")
        if not data['departure'][1:].islower():
            raise forms.ValidationError("The only capital letter should"
                                        " be the first one")
        return data['departure']

    def clean_arrival(self):
        data = self.cleaned_data
        if not data['arrival'][0].isupper():
            raise forms.ValidationError("Arrival location"
                                        " shold start with a capital letter")
        if not data['departure'][1:].islower():
            raise forms.ValidationError("The only capital letter should"
                                        " be the first one")
        return data['arrival']

    def clean_departure_date(self):
        data = self.cleaned_data
        if data['departure_date'] < date.today():
            raise forms.ValidationError("Enter a valid date")
        return data['departure_date']

    def clean_arrival_date(self):
        data = self.cleaned_data
        if data['arrival_date'] < date.today():
            raise forms.ValidationError("Enter a valid date")
        elif data['arrival_date'] < data['departure_date']:
            raise forms.ValidationError("Arrival can't be"
                                        " before departure date")
        return data['arrival_date']

    def clean_arrival_time(self):
        data = self.cleaned_data
        if data['arrival'] == data['departure']:
            if data['arrival_time'] > data['departure_time']:
                raise forms.ValidationError("If departure and arrival"
                                            " are at the same date arrival"
                                            " time should be after departure"
                                            " time")
        return data['arrival_time']
