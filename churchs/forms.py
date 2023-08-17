from django import forms

from .models import Churchs, SYNOD, TYPE
from places.models import Places

class ChurchsForm(forms.ModelForm):
    country = forms.ModelChoiceField(queryset=Places.objects.values_list('country', flat=True).distinct(), required=False)
    district = forms.ModelChoiceField(queryset=Places.objects.none(), required=False)
    neighborhood = forms.ModelChoiceField(queryset=Places.objects.none(), required=False)
    street = forms.ModelChoiceField(queryset=Places.objects.none(), required=False)

    class Meta:
        model = Churchs
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['church_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['church_branch'].widget.attrs.update({'class': 'form-control'})
        self.fields['church_tree'].widget.attrs.update({'class': 'form-control'})
        self.fields['church_synod'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_of'].widget.attrs.update({'class': 'form-control'})
        self.fields['located_at'].widget.attrs.update({'class': 'form-control'})
        
        # Call the methods to populate the choices for the dependent fields
        self.fields['country'].choices = self.get_country_choices()
        
        # Initialize the district choices
        country_value = self.initial.get('country')  # Get the initial value of the country field
        if country_value:
            self.fields['district'].queryset = Places.objects.filter(country=country_value).values_list('district', flat=True).distinct()

        # Initialize the neighborhood choices
        district_value = self.initial.get('district')  # Get the initial value of the district field
        if district_value:
            self.fields['neighborhood'].queryset = Places.objects.filter(district=district_value).values_list('neighborhood', flat=True).distinct()

        # Initialize the street choices
        neighborhood_value = self.initial.get('neighborhood')  # Get the initial value of the neighborhood field
        if neighborhood_value:
            self.fields['street'].queryset = Places.objects.filter(neighborhood=neighborhood_value).values_list('street', flat=True).distinct()
    
        
    def get_country_choices(self):
        countries = Places.objects.values_list('country', flat=True).distinct()
        return [(country, country) for country in countries]
    
    def get_district_choices(self):
        country = self.initial.get('country') or self['country'].value()
        if country:
            districts = Places.objects.filter(country=country).values_list('district', flat=True).distinct()
            return [(district, district) for district in districts]
        return []

    def get_neighborhood_choices(self):
        district = self.initial.get('district') or self['district'].value()
        if district:
            neighborhoods = Places.objects.filter(district=district).values_list('neighborhood', flat=True).distinct()
            return [(neighborhood, neighborhood) for neighborhood in neighborhoods]
        return []

    def get_street_choices(self):
        neighborhood = self.initial.get('neighborhood') or self['neighborhood'].value()
        if neighborhood:
            streets = Places.objects.filter(neighborhood=neighborhood).values_list('street', flat=True).distinct()
            return [(street, street) for street in streets]
        return []