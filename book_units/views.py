from .serializers import Get_units_serializer,Booked_units_serializer
from .models import Selected_units,Units

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# get all users
class Get_Units(APIView):
    def get(self,request):
        queryset=Units.objects.all()
        serializer=Get_units_serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

# save selected units by user
class Set_selected_units(APIView):
    def post(self,request):
        for value in request.data:
            serializer=Booked_units_serializer(data=value)
            if serializer.is_valid():
                if not Selected_units.objects.filter(unit_code=serializer.validated_data['unit_code']).exists():               
                    serializer.save()
        return Response(request.data,status=status.HTTP_201_CREATED)

# get all selected units by user
class GetSelectedUnits(APIView):
    def get(self,requet):
        queryset=Selected_units.objects.all()
        serializer=Booked_units_serializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




# Create your views here.

