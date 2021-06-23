from rest_framework import serializers

from .models import Math

class MathSerializer(serializers.ModelSerializer):

    class Meta:
        model = Math
        fields = '__all__'