from django.db.models.signals import pre_save
from django.dispatch import receiver

from ..models import Result


def assign_grade(score):
    if(score <= 100 and score >= 70):
        return "A"
    elif(score < 70 and score >= 60):
        return "B"
    elif(score < 60 and score >= 50):
        return "C"
    elif(score < 50 and score >= 40):
        return "D"
    else:
        return "F"


@receiver(pre_save, sender=Result)
def set_Grade(sender, instance, **kwargs):
    instance.grade = assign_grade(instance.marks)
