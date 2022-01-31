from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
# from .serializers import ResultsSerializer

    
# get student results
class Student_result(APIView):
    def get(self,request):
        queryset=Result.objects.select_related('unit')
        # serializer=ResultsSerializer(queryset,many=True)
        array_queryset=[]
        for object in queryset:
            data={
                "unit_name":object.unit.unit_name,
                "unit_code":object.unit.unit_code,
                "year":object.unit.year,
                "marks":object.marks,
                "grade":object.grade
            }
            array_queryset.append(data)
        # return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(array_queryset)
               
# Create your views here.
