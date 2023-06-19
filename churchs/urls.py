from django.urls import path
from .views import *

urlpatterns = [
    # churchs urls
    path('', church_view, name='churchs'),
    path('add/', church_add, name='add_church'),
    path('<int:pk>/edit/', church_edit, name='edit_church'),
    path('<int:pk>/delete/', church_delete, name='church_delete'),
    
]