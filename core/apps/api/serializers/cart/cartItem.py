from rest_framework import serializers

from core.apps.api.models import CartitemModel, ProductModel
from core.apps.api.serializers.product.product import BaseProductSerializer


class BaseCartitemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    cart = serializers.SerializerMethodField()
    
    class Meta:
        model = CartitemModel
        fields = [
            "id",
            "cart",
            "product",
            "quantity",
            "total_price"
        ]
        
    def get_product(self, obj):
        return BaseProductSerializer(obj.product).data
    
    def get_cart(self, obj):
        from core.apps.api.serializers.cart import BaseCartSerializer
        return BaseCartSerializer(obj.cart).data


class ListCartitemSerializer(serializers.ModelSerializer):
    title =serializers.CharField(source="product.title")
    image_id = serializers.CharField(source="product.image_id")
    price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField()
    
    class Meta:
        model = CartitemModel
        fields = [
            "id",
            "title",
            "image_id",
            "price",
            "quantity"
        ]


class RetrieveCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class CreateCartitemSerializer(BaseCartitemSerializer):
    title = serializers.CharField(source="product.title", read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())
    
    
    class Meta(BaseCartitemSerializer.Meta):
        fields = [
            "title",
            "product",
            "quantity",
        ]
