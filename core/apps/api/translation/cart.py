from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CartitemModel, CartModel


@register(CartModel)
class CartTranslation(TranslationOptions):
    fields = []


@register(CartitemModel)
class CartitemTranslation(TranslationOptions):
    fields = []
