from import_export import resources
from .models import Orgs


class OrgsResource(resources.ModelResource):
    class Meta:
        model = Orgs
