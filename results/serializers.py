from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    user_name=serializers.ReadOnlyField(source='user.username')
    email=serializers.ReadOnlyField(source='user.email')
    unit_name=serializers.ReadOnlyField(source='unit.unit_name')
    unit_code=serializers.ReadOnlyField(source='unit.unit_code')
    class Meta:
        model=Result
        fields=['user_name','marks','grade','email','unit_name','unit_code']
        ordering=['id']

