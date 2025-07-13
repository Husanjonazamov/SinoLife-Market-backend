from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CartModel(AbstractBaseModel):

    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "cart"
        verbose_name = _("CartModel")
        verbose_name_plural = _("CartModels")


class CartitemModel(AbstractBaseModel):

    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "cartItem"
        verbose_name = _("CartitemModel")
        verbose_name_plural = _("CartitemModels")
