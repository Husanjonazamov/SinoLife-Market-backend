from django.contrib.auth import models as auth_models
from django.db import models

from ..choices import RoleChoice
from ..managers import UserManager
from django.utils.translation import gettext_lazy as _
from core.apps.api.enums.choices import LangChoices



class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True, blank=True, null=True)
    tg_id = models.BigIntegerField(blank=True, null=True)
    lang = models.CharField(verbose_name=_("Lang"), choices=LangChoices.choices, default=LangChoices.UZBEK)
    
    username = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.USER,
    )

    USERNAME_FIELD = "phone"
    objects = UserManager()

    def __str__(self):
        return self.phone
