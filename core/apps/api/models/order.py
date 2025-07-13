from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class OrderModel(AbstractBaseModel):

    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")


class OrderitemModel(AbstractBaseModel):

    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "orderItem"
        verbose_name = _("OrderitemModel")
        verbose_name_plural = _("OrderitemModels")
