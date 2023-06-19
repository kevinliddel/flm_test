from django.urls import path
from .views import *

urlpatterns = [
    # ministries urls
    path('', ministry_view, name='ministries'),
    path('add/', ministry_add, name='add_ministry'),
    path('<int:pk>/edit/', ministry_edit, name='edit_ministry'),
    path('<int:pk>/delete/', ministry_delete, name='ministry_delete'),
    
]