from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CartModel(AbstractBaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, blank=True, null=True)
    total_price = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return str(self.user.first_name)

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
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, related_name="cart")
    product = models.ForeignKey("api.ProductModel", on_delete=models.CASCADE, related_name="product")
    quantity = models.PositiveBigIntegerField(verbose_name=_("Quantity"))
    total_price = models.DecimalField(max_digits=200, decimal_places=2)

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
