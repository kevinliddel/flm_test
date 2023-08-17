from django.urls import path
from .views import *

urlpatterns = [
    # places urls
    path('', place_view, name='places'),
    path('import/', importExcel, name='place'),   
    path('get_districts', get_districts, name='get_districts'),
    path('get_neighborhoods', get_neighborhoods, name='get_neighborhoods'), 
    path('get_streets', get_streets, name='get_streets'), 
    path('dependant_list', dependant_select_list_view, name='dependant_list')
]
