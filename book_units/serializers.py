from select import select
from httpcore import request
from rest_framework import serializers

from .models import BookedUnit,Unit

class Get_units_serializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields=['id','year','unit_name','unit_code']

class Booked_units_serializer(serializers.ModelSerializer):    
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=BookedUnit
        fields=['id','user','unit_name','unit_code','year']
    