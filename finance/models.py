from django.db import models
from django.contrib.auth.models import User

class FeeModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    total_fee=models.IntegerField(default=100000)
    paid_fee=models.IntegerField()
    remaining_fee=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}({self.paid_fee})'


# Create your models here.
