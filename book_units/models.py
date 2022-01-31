from django.db import models

class Units(models.Model):
    YEAR_CHOICES=[
    ('y1s1','First year:sem 1'),
    ('y1s2','First year:sem 2'),
    ('y2s1','Second year:sem 1'),
    ('y2s2','Second year:sem 2'),
    ('y3s1','Third year:sem 1'),
    ('y3s2','Third year:sem 2'),
    ('y4s1','Fourth year:sem 1'),
    ('y4s2','Fourth year:sem 2')
    ] 
    year=models.CharField(default='y1s1',choices=YEAR_CHOICES,max_length=20)
    unit_name=models.CharField(max_length=200)
    unit_code=models.CharField(max_length=10)
    def __str__(self):
        return self.unit_name

# Create your models here.


class Selected_units(models.Model):
    YEAR_CHOICES=[
    ('y1s1','First year:sem 1'),
    ('y1s2','First year:sem 2'),
    ('y2s1','Second year:sem 1'),
    ('y2s2','Second year:sem 2'),
    ('y3s1','Third year:sem 1'),
    ('y3s2','Third year:sem 2'),
    ('y4s1','Fourth year:sem 1'),
    ('y4s2','Fourth year:sem 2')
    ] 
    year=models.CharField(default='y1s1',choices=YEAR_CHOICES,max_length=20)
    unit_name=models.CharField(max_length=200)
    unit_code=models.CharField(max_length=10)
    def __str__(self):
        return self.unit_name

