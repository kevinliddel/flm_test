from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import (
    PlacesForm
)
from .models import Places
from .resources import PlacesResource
from tablib import Dataset

# Create your views here.
def place_view(request):
    places = Places.objects.all()
    paginator = Paginator(places, 10)
    page_number = request.GET.get('page')
    places = paginator.get_page(page_number)
    
    place_filter = request.GET.get('place_filter')
    if place_filter:
        places = Places.objects.filter(name__icontains=place_filter)
        
    return render(request, 'places/place_list.html', {
        'title': "Liste des localités",
        'places': places,
    })
    
def importExcel(request):
    if request.method == 'POST':
        places_resource = PlacesResource()
        dataset = Dataset()
        new_places = request.FILES['places_file']
        imported_data = dataset.load(new_places.read(), format='xlsx')
        for data in imported_data:
            value = Places(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            )
            if value.is_valid():
                value.save()
                messages.success(request, 'Le fichier a bien été importé')
                return redirect('places')
                
    
    return render(request, 'places/place_add.html', {
        'title': "Importer les localités"
    })