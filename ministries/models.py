from django.db import models
from django.db.models import Q

MALE = "Homme"
FEMALE = "Femme"

SEX = (
    (MALE, "Homme"),
    (FEMALE, "Femme"),
)


class MinistriesManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                         Q(surname__icontains=query)| 
                         Q(service__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
    

class Ministries(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    birth = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    birthplace = models.CharField(max_length=200, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=200, choices=SEX, blank=True, null=True, default="Homme")
    service = models.CharField(max_length=200, null=True)
    works_at = models.CharField(max_length=200, null=True)
    debuted_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    
    objects = MinistriesManager()

    def __str__(self):
        return self.name
    