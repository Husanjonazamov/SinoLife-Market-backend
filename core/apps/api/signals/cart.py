from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import CartitemModel, CartModel


@receiver(post_save, sender=CartModel)
def CartSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=CartitemModel)
def CartitemSignal(sender, instance, created, **kwargs): ...
