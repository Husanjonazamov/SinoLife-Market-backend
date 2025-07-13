from django import forms

from core.apps.api.models import OrderitemModel, OrderModel


class OrderForm(forms.ModelForm):

    class Meta:
        model = OrderModel
        fields = "__all__"


class OrderitemForm(forms.ModelForm):

    class Meta:
        model = OrderitemModel
        fields = "__all__"
