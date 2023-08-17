from django import forms

from .models import Sacraments, SEX
from places.models import Places

class SacramentsForm(forms.ModelForm):  
    country = forms.ChoiceField(required=False)
    district = forms.ChoiceField(required=False)
    neighborhood = forms.ChoiceField(required=False)
    street = forms.ChoiceField(required=False)
    
    class Meta:
        model = Sacraments
        fields = '__all__'
    

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthplace'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['sex'].widget.attrs.update({'class': 'form-control'})
        self.fields['father'].widget.attrs.update({'class': 'form-control'})
        self.fields['mother'].widget.attrs.update({'class': 'form-control'})
        self.fields['familytree'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['birth'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['sacrament_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    
        self.fields['country'].choices = self.get_country_choices()

    def get_country_choices(self):
        countries = Places.objects.values_list('country', flat=True).distinct()
        return [("", "Choisissez une région")] + [(country, country) for country in countries]

    def get_district_choices(self, country):
        districts = Places.objects.filter(country=country).values_list('district', flat=True).distinct()
        return [("", "Choisissez un district")] + [(district, district) for district in districts]

    def get_neighborhood_choices(self, district):
        neighborhoods = Places.objects.filter(district=district).values_list('neighborhood', flat=True).distinct()
        return [("", "Choisissez une commune")] + [(neighborhood, neighborhood) for neighborhood in neighborhoods]

    def get_street_choices(self, neighborhood):
        streets = Places.objects.filter(neighborhood=neighborhood).values_list('street', flat=True).distinct()
        return [("", "Choisissez un quartier")] + [(street, street) for street in streets]
