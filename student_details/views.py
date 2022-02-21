from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserCredentialsSerializer
from .models import StudentDetailsModel
from rest_framework import status


# get each individual users details
class GetUserCredentials(APIView):
    def get(self,request):
        try:
            queryset=StudentDetailsModel.objects.get(user__username=request.user)
            serializer=UserCredentialsSerializer(queryset)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception:
            return Response({'error':"your details dont exist in the database"})


# Create your views here.
