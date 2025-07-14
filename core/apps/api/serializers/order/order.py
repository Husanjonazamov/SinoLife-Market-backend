from rest_framework import serializers
from core.apps.accounts.models.user import User
from core.apps.api.serializers.order.orderItem import BaseOrderitemSerializer

from core.apps.api.models import OrderModel, CartModel, OrderitemModel
from core.apps.payment.enums.send_generate import send_generate_payment


class BaseOrderSerializer(serializers.ModelSerializer):
    order_items = BaseOrderitemSerializer(many=True, read_only=True)
    class Meta:
        model = OrderModel
        fields = [
            "id",
            "user",
            "total",
            "payment_type",
            "status",
            "order_items"
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(serializers.ModelSerializer):
    tg_id = serializers.CharField(write_only=True)

    class Meta:
        model = OrderModel
        fields = ["id", "tg_id", "payment_type"]

    def validate(self, attrs):
        tg_id = attrs.pop("tg_id")
        try:
            user = User.objects.get(tg_id=tg_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"tg_id": "foydalanuvchi topilmadi."})
        
        attrs["user"] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.get("user")
        payment_type = validated_data.get("payment_type")
        
        try:
            cart = CartModel.objects.get(user=user)
        except CartModel.DoesNotExist:
            raise serializers.ValidationError({"cart": "Savatingiz bo‘sh."})

        order = OrderModel.objects.create(
            user=user,
            total=cart.total_price,
            payment_type=payment_type
        )
        send_generate_payment(order)
        
        
        for item in cart.cart_item.all():
            OrderitemModel.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.total_price
            )

        cart.cart_item.all().delete()
        cart.total_price = 0
        cart.save()

        return order
