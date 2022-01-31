from rest_framework.serializers import ModelSerializer
from .models import StudentDetailsModel
from django.contrib.auth.models import User
class UserCredentialsSerializer(ModelSerializer):
    class Meta:
        model=StudentDetailsModel
        fields=['id','school_id','school_email','gender','country','city','phone']