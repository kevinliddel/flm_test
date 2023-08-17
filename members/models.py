from django.db import models
from django.db.models import Q


MALE = "Homme"
FEMALE = "Femme"

SEX = (
    (MALE, "Homme"),
    (FEMALE, "Femme"),
)

MARRIED = "Marié(e)"
WIDOW = "Veuf(ve)"
SINGLE = "Célibataire"

SITUATION = (
    (MARRIED, "Marié(e)"),
    (WIDOW, "Veuf(ve)"),
    (SINGLE, "Célibataire")
)

class MembersManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) | 
                         Q(surname__icontains=query)| 
                         Q(familytree__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
    

class Members(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True)
    birth = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    birthplace = models.CharField(max_length=200, null=True)
    age = models.IntegerField(blank=True, null=True)
    sex = models.CharField(max_length=200, choices=SEX, blank=True, null=True, default="Homme")
    job = models.CharField(max_length=200, null=True)
    diploma = models.CharField(max_length=200, null=True)
    baptism = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    sacrament = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    faction = models.CharField(max_length=200, null=True)
    situation = models.CharField(max_length=200, choices=SITUATION, blank=True, null=True, default="Célibataire")
    engagement = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    marriage = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    familytree = models.CharField(max_length=200, null=True)
    
    objects = MembersManager()

    def __str__(self):
        return self.name
    