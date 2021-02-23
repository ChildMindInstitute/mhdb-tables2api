from rest_framework import serializers
from disorders.models import DisorderCategory

class DisorderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DisorderCategory
        fields = '__all__'
