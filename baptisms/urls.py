from django.urls import path
from .views import *

urlpatterns = [
    # baptisms urls
    path('', baptism_view, name='baptisms'),
    path('add/', baptism_add, name='add_baptism'),
    path('<int:pk>/edit/', baptism_edit, name='edit_baptism'),
    path('<int:pk>/delete/', baptism_delete, name='baptism_delete'),
    
]