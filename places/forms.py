from django import forms
from .models import Places

from django.utils.translation import gettext_lazy as _

import re

class PlacesForm(forms.Form):
    class meta:
        model = Places
        fields = '__all__'
        
    