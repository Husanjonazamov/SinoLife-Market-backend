from rest_framework import serializers
from core.apps.api.serializers.product import BaseProductSerializer

from core.apps.api.models import OrderitemModel, ProductModel


class BaseOrderitemSerializer(serializers.ModelSerializer):
    product = BaseProductSerializer()
    
    class Meta:
        model = OrderitemModel
        fields = [
            "id",                                   
            "order",
            "product",
            "quantity",
            "price"
        ]


class ListOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class RetrieveOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class CreateOrderitemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())
    class Meta:
        model = OrderitemModel
        fields = [
            "id",
            "product",
            "quantity",
            "price"
        ]
