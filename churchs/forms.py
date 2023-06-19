from django import forms

from .models import Churchs, SYNOD

class ChurchsForm(forms.ModelForm):  
    class Meta:
        model = Churchs
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['church_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['church_branch'].widget.attrs.update({'class': 'form-control'})
        self.fields['church_tree'].widget.attrs.update({'class': 'form-control'})
        self.fields['church_synod'].widget.attrs.update({'class': 'form-control'})
        self.fields['located_at'].widget.attrs.update({'class': 'form-control'})

    