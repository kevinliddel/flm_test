from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .forms import (
    PlacesForm
)
from .models import Places
from .resources import PlacesResource
from tablib import Dataset
from django.http import JsonResponse

# Create your views here.
@login_required
@never_cache
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
    
@login_required
@never_cache
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
            try:
                value.full_clean()  # Manually trigger model validation
            except ValidationError as e:
                messages.error(request, f"Invalid data: {e}")
                return redirect('places')
            
            value.save()
                
    
    return render(request, 'places/place_add.html', {
        'title': "Importer les localités",
    })

def get_districts(request):
    country_name = request.GET.get('country_name')
    districts = Places.objects.filter(country=country_name).values('district').distinct()
    return JsonResponse(list(districts), safe=False)

def get_neighborhoods(request):
    district_name = request.GET.get('district_name')
    neighborhoods = Places.objects.filter(district=district_name).values('neighborhood').distinct()
    return JsonResponse(list(neighborhoods), safe=False)

def get_streets(request):
    neighborhood_name = request.GET.get('neighborhood_name')
    streets = Places.objects.filter(neighborhood=neighborhood_name).values('street').distinct()
    return JsonResponse(list(streets), safe=False)

def dependant_select_list_view(request):
    countries = Places.objects.values_list('country', flat=True).distinct()
    return render(request, 'places/dependant_select_list.html', {
        'title': "Localités par région",
        'countries': countries
    })
    