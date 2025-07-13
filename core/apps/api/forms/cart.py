from django import forms

from core.apps.api.models import CartitemModel, CartModel


class CartForm(forms.ModelForm):

    class Meta:
        model = CartModel
        fields = "__all__"


class CartitemForm(forms.ModelForm):

    class Meta:
        model = CartitemModel
        fields = "__all__"
