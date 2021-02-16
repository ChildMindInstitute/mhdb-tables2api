from rest_framework import viewsets

from assessments.models import Questionnaire, Author
from assessments.serializers import QuestionnaireSerializer, AuthorSerializer

class AuthorViewset(viewsets.ModelViewSet):
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

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class QuestionnaireViewset(viewsets.ModelViewSet):
    """
    list:
    return the records for questionaires.
    
    create:
    add a new questionaire to the database. Make sure to check first that the new record is 
    genuinely new and that a similar name does not already exist.

    read:
    look up a specific record by id number

    update:
    change the fields value for a specific record. For example to correct a misspelling.
    """

    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


