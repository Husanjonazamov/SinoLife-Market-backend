from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ProductModel


@register(ProductModel)
class ProductTranslation(TranslationOptions):
    fields = [
        "title",
        "description"
    ]
