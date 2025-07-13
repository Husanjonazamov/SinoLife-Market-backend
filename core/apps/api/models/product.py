from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ProductModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    category = models.ForeignKey("api.ProductModel", on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=100, decimal_places=2)
    image_id = models.CharField(verbose_name=_("Image ID"), max_length=255, blank=True, null=True)
    video_id = models.CharField(verbose_name=_("Video ID"), max_length=255, blank=True, null=True)
    

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "product"
        verbose_name = _("ProductModel")
        verbose_name_plural = _("ProductModels")
