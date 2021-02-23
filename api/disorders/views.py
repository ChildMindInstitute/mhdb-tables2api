from django.shortcuts import render
from rest_framework import viewsets

from disorders.models import DisorderCategory
from disorders.serializers import DisorderCategorySerializer


class DisorderCategoryViewset(viewsets.ModelViewSet):
    """
    list:
    return the all records (paginated)
    
    create:
    add a new record to the database

    read:
    look up a specific record by id number

    update:
    change the fields value for a specific record. For example to correct a misspelling.
    """

    queryset = DisorderCategory.objects.all()
    serializer_class = DisorderCategorySerializer