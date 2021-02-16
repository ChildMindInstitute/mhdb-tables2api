from rest_framework import viewsets

from resources.models import Language
from resources.serializers import LanguageSerializer

class LanguageViewset(viewsets.ModelViewSet):
    """
    list:
    return the all records
    
    create:
    add a new record to the database

    read:
    look up a specific record by id number

    update:
    change the fields value for a specific record. For example to correct a misspelling.
    """

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer