from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('flm/', views.homepage, name='homepage'),
        path('accounts/', include("django.contrib.auth.urls")),
]
