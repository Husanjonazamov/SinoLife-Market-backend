from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


from core.apps.api.enums.choices import OrderPaymentChoice, OrderStatusChoice



class OrderModel(AbstractBaseModel):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="user") 
    total = models.DecimalField(max_digits=100, decimal_places=2)
    payment_type = models.CharField(max_length=200, choices=OrderPaymentChoice.choices, default=OrderPaymentChoice.PAYME)
    status = models.CharField(max_length=100, choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING)
       

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
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey("api.ProductModel", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    

    def __str__(self):
        return str(self.product.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "orderItem"
        verbose_name = _("OrderitemModel")
        verbose_name_plural = _("OrderitemModels")
