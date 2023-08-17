from django import forms

from members.models import Members
# from dal import autocomplete
from django.contrib.admin import widgets
from .models import Baptisms, SEX
from places.models import Places


class BaptismsForm(forms.ModelForm):  
    country = forms.ChoiceField(required=False)
    district = forms.ChoiceField(required=False)
    neighborhood = forms.ChoiceField(required=False)
    street = forms.ChoiceField(required=False)
    
    class Meta:
        model = Baptisms
        fields = '__all__'
        
    
#    father_name = forms.ModelChoiceField(
#        queryset = Members.objects.all(),
#        widget=autocomplete.ModelSelect2(
#            url='father-autocomplete',
#            attrs={
#                'data-placeholder': ' ',
#                'data-minimum-input-length': 1,
#            }
#        )
#    )
    
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
        self.fields['responsible'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['birth'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['baptism_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        
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
    
    

    def clean(self):
        cleaned_data = super().clean()
        country = cleaned_data.get('country')
        district = cleaned_data.get('district')
        neighborhood = cleaned_data.get('neighborhood')
        street = cleaned_data.get('street')

        # Perform any validation or additional data processing as needed
        # For example, you can check if the fields are not empty or if the data is valid.

        return cleaned_data
    