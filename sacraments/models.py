from django.db import models
from django.db.models import Q

MALE = "Homme"
FEMALE = "Femme"

SEX = (
    (MALE, "Homme"),
    (FEMALE, "Femme"),
)

class SacramentsManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                         Q(surname__icontains=query)| 
                         Q(familytree__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
    

class Sacraments(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    birth = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    birthplace = models.CharField(max_length=200, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=200, choices=SEX, blank=True, null=True, default="Homme")
    sacrament_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    father = models.CharField(max_length=200, null=True)
    mother = models.CharField(max_length=200, null=True)
    familytree = models.CharField(max_length=200, null=True)
    
    country = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    
    objects = SacramentsManager()

    def __str__(self):
        return self.name
    