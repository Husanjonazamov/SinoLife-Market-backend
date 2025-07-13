from rest_framework import serializers

from core.apps.api.models import CartitemModel


class BaseCartitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartitemModel
        fields = [
            "id",
            "name",
        ]


class ListCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class RetrieveCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class CreateCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
