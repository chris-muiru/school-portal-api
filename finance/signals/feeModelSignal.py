from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import FeeModel

@receiver(pre_save, sender=FeeModel)
def set_remaining_fee(sender, instance,**kwargs):
    instance.remaining_fee = (instance.total_fee - instance.paid_fee)