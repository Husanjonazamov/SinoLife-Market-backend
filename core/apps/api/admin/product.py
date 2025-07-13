from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import ProductModel



@admin.register(ProductModel)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "price"
    )
