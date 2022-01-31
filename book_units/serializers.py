from rest_framework import serializers

from .models import Selected_units,Units

class Get_units_serializer(serializers.ModelSerializer):
    class Meta:
        model=Units
        fields=['id','year','unit_name','unit_code']


class Booked_units_serializer(serializers.ModelSerializer):
    class Meta:
        model=Selected_units
        fields=['id','year','unit_name','unit_code']
