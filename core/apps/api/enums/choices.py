from django.db import models
from django.utils.translation import gettext_lazy as _






class LangChoices(models.TextChoices):
    UZBEK = 'uz', 'Uzbek'
    ENGLISH = 'en', 'English'
    RUSSIAN = 'ru', 'Russian'
    



class OrderPaymentChoice(models.TextChoices):
    CLICK = "click", _("CLICK")
    PAYME = "payme", _("PAYME")
    


class OrderStatusChoice(models.TextChoices):
    PENDING = "pending", "Kutilmoqda"
    PAID = "paid", "To‘langan"
    CANCELLED = "cancelled", "Bekor qilingan"

    
    
