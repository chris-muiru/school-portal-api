from rest_framework.response import Response
from rest_framework import  generics
from rest_framework import status
from .models import FeeModel
from .serializers import FeeDetailsSerializer

class GetFeeDetailsView(generics.ListAPIView):
    queryset=FeeModel.objects.all()
    serializer_class=FeeDetailsSerializer




# Create your views here.
