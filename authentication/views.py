from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

class register_user(APIView):
    def post(self,request): 
        serializer=RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfully registered a new user"
            data['email'] = account.email
            data['username'] = account.username
            token=Token.objects.get(user=account).key
            data['token'] = token
        return Response(data)
# Create your views here.
