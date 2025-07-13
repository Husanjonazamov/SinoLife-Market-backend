from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import OrderitemModel, OrderModel


@register(OrderModel)
class OrderTranslation(TranslationOptions):
    fields = []


@register(OrderitemModel)
class OrderitemTranslation(TranslationOptions):
    fields = []
