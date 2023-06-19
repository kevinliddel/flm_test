from django import forms

from .models import Sacraments, SEX

class SacramentsForm(forms.ModelForm):  
    class Meta:
        model = Sacraments
        exclude = ['birth', 'sacrament_date']
    

    
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
    