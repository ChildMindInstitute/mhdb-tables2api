from rest_framework import serializers
from disorders.models import DisorderCategory, Disorder

class DisorderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DisorderCategory
        fields = '__all__'

class DisorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disorder
        fields = '__all__'
