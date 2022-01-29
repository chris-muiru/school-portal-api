from rest_framework.serializers import ModelSerializer
from .models import UserCredentialsModel
from django.contrib.auth.models import User
class UserCredentialsSerializer(ModelSerializer):
    class Meta:
        model=UserCredentialsModel
        fields=['id','school_id','school_email','gender','country','city','phone']