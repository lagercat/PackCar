from datetime import date

from django import forms

from .models import Package


class PackageForm(forms.ModelForm):
    class Meta:
        instance = Package
        fields = ['title', 'details', 'departure', 'arrival',
                  'departure_date', 'arrival_date']

    def clean_title(self):
        data = self.cleaned_data
        if data['title'].isdigit():
            raise forms.ValidationError("Title can't be numeric")
        if len(data['title']) < 10:
            raise forms.ValidationError("Title has to be at least"
                                        "10 characters long")

    def clean_description(self):
        data = self.cleaned_data
        if data['details'].isdigit():
            raise forms.ValidationError("Details can't be numeric")
        if len(data['details']) < 40:
            raise forms.ValidationError("Details has to be at least"
                                        "40 characters long")

    def clean_departure(self):
        data = self.cleaned_data
        if not data['departure'][0].isupper():
            raise forms.validators("Departure location"
                                   "should start wtih capital letter")
        if not data['departure'][1:].islower():
            raise forms.ValidationError("The only capital letter should"
                                        "be the first one")
        return data['departure']

    def clean_arrival(self):
        data = self.cleaned_data
        if not data['arrival'][0].isupper():
            raise forms.ValidationError("Arrival location"
                                        "shold start with a capital letter")
        if not data['departure'][1:].islower():
            raise forms.ValidationError("The only capital letter should"
                                        "be the first one")
        return data['arrival']

    def clean_departure_date(self):
        data = self.cleaned_data
        if data['departure_date'] < date.now():
            raise forms.ValidationError("Enter a valid date")
        return data['departure_date']

    def clean_arrival_date(self):
        data = self.cleaned_data
        if data['arrival_date'] < data.now():
            raise forms.ValidationError("Enter a valid date")
        elif data['arrival_date'] < data['departure_date']:
            raise forms.ValidationError("Arrival can't be"
                                        "before departure date")
        return data['arrival_date']
