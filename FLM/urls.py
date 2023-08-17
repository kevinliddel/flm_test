from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('statistic.urls')),
    path('members/', include('members.urls')),
    path('places/', include('places.urls')),
    path('ministries/', include('ministries.urls')),
    path('churchs/', include('churchs.urls')),
    path('baptisms/', include('baptisms.urls')),
    path('sacraments/', include('sacraments.urls')),
    path('search/', include('search.urls')),
    path('users/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
