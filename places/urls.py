from django.urls import path
from .views import *

urlpatterns = [
    # places urls
    path('', place_view, name='places'),
    path('import/', importExcel, name='place'),   
]
