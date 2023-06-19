from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('statistic.urls')),
    path('members/', include('members.urls')),
    path('places/', include('places.urls')),
    path('ministries/', include('ministries.urls')),
    path('churchs/', include('churchs.urls')),
    path('baptisms/', include('baptisms.urls')),
    path('sacraments/', include('sacraments.urls')),
    path('', include("django.contrib.auth.urls")),
]
