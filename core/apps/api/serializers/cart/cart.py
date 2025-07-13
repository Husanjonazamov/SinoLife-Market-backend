from rest_framework import serializers

from core.apps.api.models import CartModel


class BaseCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = [
            "id",
            "name",
        ]


class ListCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class CreateCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
