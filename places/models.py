
from django.db import models
from django.db.models import Q

class PlacesManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(country__icontains=query) | 
                         Q(district__icontains=query) | 
                         Q(neighborhood__icontains=query)|
                         Q(street__icontains=query) 
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs    

class Places(models.Model):
    country = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)

    objects = PlacesManager()

    def __str__(self):
        return f"{self.country}, {self.district}, {self.neighborhood}; {self.street}"
    