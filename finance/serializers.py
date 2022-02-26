from rest_framework.serializers import ModelSerializer
from .models import FeeModel
from rest_framework import serializers

class FeeDetailsSerializer(ModelSerializer):
    class Meta:
        model=FeeModel
        fields=['total_fee','paid_fee','remaining_fee']
