from rest_framework.serializers import ModelSerializer
from .models import FeeModel
from rest_framework import serializers

class FeeDetailsSerializer(ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=FeeModel
        fields=['user','total_fee','paid_fee','remaining_fee']
