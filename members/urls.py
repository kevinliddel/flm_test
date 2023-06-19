from django.urls import path
from .views import *

urlpatterns = [
    # members urls
    path('', member_view, name='members'),
    path('add/', member_add, name='add_member'),
    path('<int:pk>/edit/', member_edit, name='edit_member'),
    path('<int:pk>/delete/', member_delete, name='member_delete'),
    
]
