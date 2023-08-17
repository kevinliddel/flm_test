from django import forms

from .models import Members, SEX, SITUATION

class MembersForm(forms.ModelForm):  
    class Meta:
        model = Members
        exclude = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthplace'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['sex'].widget.attrs.update({'class': 'form-control'})
        self.fields['job'].widget.attrs.update({'class': 'form-control'})
        self.fields['diploma'].widget.attrs.update({'class': 'form-control'})
        self.fields['faction'].widget.attrs.update({'class': 'form-control'})
        self.fields['situation'].widget.attrs.update({'class': 'form-control'})
        self.fields['familytree'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['birth'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['baptism'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['sacrament'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['engagement'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['marriage'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    