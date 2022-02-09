from rest_framework.exceptions import ValidationError
from .serializers import Get_units_serializer,Booked_units_serializer
from .models import BookedUnit,Unit
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .serializers import Booked_units_serializer
from rest_framework import permissions
from rest_framework import  generics

from book_units import serializers

class Get_Units(generics.ListAPIView):
    querset=Unit.objects.all()
    serializer_class=Get_units_serializer

class SetSelectedUnits(generics.CreateAPIView):
    serializer_class=Booked_units_serializer
    def get_queryset(self):
        queryset=BookedUnit.objects.filter(user=self.request.user)
        return queryset
    def perform_create(self,serializer):
        if BookedUnit.objects.filter(unit_code=serializer.validated_data['unit_code']).exists():
            raise ValidationError("already selected unit")
        serializer.save(user=self.request.user)
   
class GetSelectedUnits(generics.ListAPIView):
    serializer_class=Booked_units_serializer
    def get_queryset(self):
        queryset=BookedUnit.objects.filter(user=self.request.user)
        return queryset
 

# Create your views here.

