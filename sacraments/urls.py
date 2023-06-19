from django.urls import path
from .views import *

urlpatterns = [
    # sacraments urls
    path('', sacrament_view, name='sacraments'),
    path('add/', sacrament_add, name='add_sacrament'),
    path('<int:pk>/edit/', sacrament_edit, name='edit_sacrament'),
    path('<int:pk>/delete/', sacrament_delete, name='sacrament_delete'),
    
]