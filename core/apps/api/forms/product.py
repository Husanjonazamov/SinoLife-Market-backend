from django import forms

from core.apps.api.models import ProductModel


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = "__all__"
