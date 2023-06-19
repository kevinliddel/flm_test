from import_export import resources
from .models import Places

class PlacesResource(resources.ModelResource):
    class meta:
        model = Places