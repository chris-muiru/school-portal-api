from rest_framework.response import Response
from rest_framework import  generics
from rest_framework import status
from .models import FeeModel
from .serializers import FeeDetailsSerializer

class GetFeeDetailsView(generics.ListAPIView):
    serializer_class=FeeDetailsSerializer
    queryset=FeeModel.objects.all()
   
    def get_queryset(self):
        return FeeModel.objects.filter(user=self.request.user)
# Create your views here.
