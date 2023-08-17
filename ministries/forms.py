from django import forms

from .models import Ministries, SEX, SERVICE

class MinistriesForm(forms.ModelForm):  
    class Meta:
        model = Ministries
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['birthplace'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['sex'].widget.attrs.update({'class': 'form-control'})
        self.fields['works_at'].widget.attrs.update({'class': 'form-control'})
        self.fields['service'].widget.attrs.update({'class': 'form-control'})
        
        self.fields['birth'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
        self.fields['debuted_at'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local'})
    