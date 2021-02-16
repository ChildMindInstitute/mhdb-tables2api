from rest_framework import serializers
from assessments.models import Questionnaire, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'

