from django.db import models
from book_units.models import BookedUnit
from django.contrib.auth.models import User
class Result(models.Model):
    unit=models.ForeignKey(BookedUnit,on_delete=models.CASCADE,default=None)    
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)    
    marks=models.IntegerField()
    grade=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.unit.unit_name}-{self.user.username}"

# Create your models here.
