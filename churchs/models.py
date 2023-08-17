from django.db import models
from django.db.models import Q

# from places.models import Places
 
SPA = "SPA - Antsiranana"
SPAVA = " SPAVA - Sambava"
SPSOFIA = "SPSofia - Antsohihy"
SPBM = "SPBM - Mahajanga"
SPAI = "SPAI - Ambatondrazaka"
SPTM = "SPTM - Toamasina"
SPANTA = "SPAnta - Antananarivo"
SPN = "SPN - Marolambo"
SPAN = "SPAN - Mananjary"
SPMA = "SPMa - Manakara"
SPATS = "SPAts - Farafangana"
SPAV = "SPAV - Vondrozo"
SPFA = "SPFa - Faradofay"
SPAA = "SPAA - Ambovombe Androy"
SPAB = "SPAB - Betroka"
SPH = "SPH - Ihosy"
SPBA = "SPBA - Betioky Atsimo"
SPFT = "SPFT - Toliara"
SPAF = "SPAf - Fianarantsoa"
SPATSIM = "SPATsim - Ambatofinandrahana"
SPM = "SPM - Morondava"
SPAFI = "SPAFI - Fandriana"
SPAM = "SPAM - Antsirabe"
SPMEL = "SPMel - Maintirano"
FLME = "FLME - Europa"

SYNOD = (
    (SPA, "SPA - Antsiranana"),
    (SPAVA, " SPAVA - Sambava"),
    (SPSOFIA, "SPSofia - Antsohihy"),
    (SPBM, "SPBM - Mahajanga"),
    (SPAI, "SPAI - Ambatondrazaka"),
    (SPTM, "SPTM - Toamasina"),
    (SPANTA, "SPAnta - Antananarivo"),
    (SPN, "SPN - Marolambo"),
    (SPAN, "SPAN - Mananjary"),
    (SPMA, "SPMa - Manakara"),
    (SPATS, "SPAts - Farafangana"),
    (SPAV, "SPAV - Vondrozo"),
    (SPFA, "SPFa - Faradofay"),
    (SPAA, "SPAA - Ambovombe Androy"),
    (SPAB, "SPAB - Betroka"),
    (SPH, "SPH - Ihosy"),
    (SPBA, "SPBA - Betioky Atsimo"),
    (SPFT, "SPFT - Toliara"),
    (SPAF, "SPAf - Fianarantsoa"),
    (SPATSIM, "SPATsim - Ambatofinandrahana"),
    (SPM, "SPM - Morondava"),
    (SPAFI, "SPAFI - Fandriana"),
    (SPAM, "SPAM - Antsirabe"),
    (SPMEL, "SPMel - Maintirano"),
    (FLME, "FLME - Europa"),
)

CHURCH = "Eglise"
HOSPITAL = "Hôpital"
CENTER = "Centre"
SCHOOL = "Ecole"

TYPE = (
    (CHURCH, "Eglise"),
    (HOSPITAL, "Hôpital"),
    (CENTER, "Centre"),
    (SCHOOL, "Ecole"),
)

class ChurchsManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(church_name__icontains=query) | 
                         Q(church_branch__icontains=query)| 
                         Q(church_tree__icontains=query)|
                         Q(church_synod__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class Churchs(models.Model):
    church_name = models.CharField(max_length=200, null=True)
    church_branch = models.CharField(max_length=200, null=True)
    church_tree = models.CharField(max_length=200, null=True)
    church_synod = models.CharField(max_length=200, choices=SYNOD, null=True)
    type_of = models.CharField(max_length=200, choices=TYPE, null=True)
    located_at = models.CharField(max_length=200, null=True)
    
    country = models.CharField(max_length=200, null=True)
    district = models.CharField(max_length=200, null=True)
    neighborhood = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    
    objects = ChurchsManager()

    def __str__(self):
        return self.church_name
    
    @classmethod
    def get_synod_counts(cls):
        return cls.objects.values('church_synod').annotate(count=models.Count('church_synod'))
    