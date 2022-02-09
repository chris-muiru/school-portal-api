from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
from .serializers import ResultSerializer
from rest_framework import status

class Student_result(APIView):
    def get(self,request):
        queryset=Result.objects.filter(user=request.user)
        serializer= ResultSerializer(queryset,many=True)     
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

# Create your views here.

