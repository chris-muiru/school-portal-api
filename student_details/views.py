import re
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCredentialsSerializer
from .models import StudentDetailsModel
from rest_framework import status

# get each individual users details
class GetUserCredentials(APIView):
    def get(self,request):
        queryset=StudentDetailsModel.objects.get(user__username=request.user)
        serializer=UserCredentialsSerializer(queryset)
        return Response(serializer.data,status=status.HTTP_200_OK)


# Create your views here.
