from rest_framework import serializers

from core.apps.api.models import ProductModel
from core.apps.api.serializers.category import ListCategorySerializer

class BaseProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "category",
            "title",
            "description",
            "price",
            "image_id",
            "video_id",
        ]

    def get_category(self, obj):
        return ListCategorySerializer(obj.category).data

class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
