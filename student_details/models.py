from django.db import models
from django.contrib.auth.models import User

class StudentDetailsModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    school_id=models.CharField(max_length=100)
    school_email=models.EmailField(max_length=254)
    CHOICES=[("male","male"),("female","female"),("non-binary","non-binary")]
    gender = models.CharField(max_length=100,choices=CHOICES)
    country=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)


    def __str__(self):
        return self.user.username


# Create your models here.
