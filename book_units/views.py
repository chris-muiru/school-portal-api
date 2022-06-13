from .serializers import Get_units_serializer, Booked_units_serializer
from .models import BookedUnit, Unit
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import Booked_units_serializer
from rest_framework import generics

from book_units import serializers


class Get_Units(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = Get_units_serializer



class SetSelectedUnits(APIView):
    def post(self, request):
        serializer = Booked_units_serializer(data=request.data, many=True)
        if serializer.is_valid():
            for queryset in serializer.data:
                if not BookedUnit.objects.filter(unit_code=queryset['unit_code']).exists():
                    serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetSelectedUnits(generics.ListAPIView):
    serializer_class = Booked_units_serializer

    def get_queryset(self):
        queryset = BookedUnit.objects.filter(user=request.user)
        return queryset


class GetUnitsInfo(APIView):
    def get(self, request):
        try:
            total_units = Unit.objects.all().count()
            booked_units = BookedUnit.objects.all().count()
            remaining_units = total_units - booked_units
            data = {
                "total_units": total_units,
                "booked_units": booked_units,
                "remaining_units": remaining_units
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "error occurred "})


# Create your views here.
