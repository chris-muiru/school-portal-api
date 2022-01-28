from django.db import models
from django.contrib.auth.models import User

class UserCredentialsModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    school_id=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=254)


# Create your models here.
