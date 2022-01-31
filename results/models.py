from django.db import models
from book_units.models import Selected_units

class Result(models.Model):
    unit=models.ForeignKey(Selected_units,on_delete=models.CASCADE,default=None)    
    marks=models.IntegerField()
    grade=models.CharField(max_length=10)

# Create your models here.
