from rest_framework import serializers
from core.apps.accounts.serializers.user import UserSerializer

from core.apps.api.models import CartModel
from decimal import Decimal
from core.apps.api.serializers.cart.cartItem import CreateCartitemSerializer, ListCartitemSerializer


# cart create
from core.apps.api.models import ProductModel, CartitemModel
from core.apps.accounts.models import User
from django.db.models import Sum


class BaseCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = [
            "id",
            "total_price"
        ]
    

class ListCartSerializer(BaseCartSerializer):
    cart_item = ListCartitemSerializer(many=True, read_only=True)
    
    class Meta(BaseCartSerializer.Meta): 
        fields = BaseCartSerializer.Meta.fields + ['cart_item']


class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...
    
    
    
class CreateCartSerializer(serializers.ModelSerializer):
    cart_item = CreateCartitemSerializer(many=True, required=True)

    class Meta:
        model = CartModel
        fields = [
            "id",
            "cart_item",
        ]

    def create(self, validated_data):
        cart_items_data = validated_data.pop("cart_item", None)

        if not cart_items_data:
            raise serializers.ValidationError({"cart_item": "cart_item bo'sh bo'lmasligi kerak"})

        request = self.context.get("request")
        tg_id = request.data.get("tg_id")
        
        try:
            user = User.objects.get(tg_id=tg_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"tg_id": "Bunday foydalanuvchi topilmadi"})
        
        cart, created = CartModel.objects.get_or_create(user=user, defaults={"total_price": 0})
        
        for item_data in cart_items_data:
            product = item_data.get("product")  
            quantity = item_data.get("quantity")
            
            price = product.price

            cart_item, created = CartitemModel.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={
                    "quantity": quantity,
                    "total_price": price * quantity
                }
            )

            if not created:
                cart_item.quantity += quantity
                cart_item.total_price = cart_item.quantity * price
                cart_item.save()

        total = CartitemModel.objects.filter(cart=cart).aggregate(
            total=Sum('total_price')
        )['total'] or 0

        cart.total_price = total
        cart.save()

        return cart
