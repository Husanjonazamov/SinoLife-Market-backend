from rest_framework import serializers

from core.apps.api.models import OrderitemModel


class BaseOrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderitemModel
        fields = [
            "id",
            "name",
        ]


class ListOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class RetrieveOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class CreateOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
