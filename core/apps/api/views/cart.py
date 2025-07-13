from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.accounts.models.user import User


from core.apps.api.models import CartitemModel, CartModel
from core.apps.api.serializers.cart import (
    CreateCartitemSerializer,
    CreateCartSerializer,
    ListCartitemSerializer,
    ListCartSerializer,
    RetrieveCartitemSerializer,
    RetrieveCartSerializer,
)

from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum



@extend_schema(tags=["cart"])
class CartView(BaseViewSetMixin, ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = ListCartSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartSerializer,
        "retrieve": RetrieveCartSerializer,
        "create": CreateCartSerializer,
    }

    def get_queryset(self):
        tg_id = self.request.query_params.get("tg_id")
        return CartModel.objects.filter(user__tg_id=tg_id)
    

    @action(detail=False, methods=['delete'], url_path="clear")
    def clear(self, request):
        tg_id = request.data.get("tg_id")
        try:
            user = User.objects.get(tg_id=tg_id)
            cart = CartModel.objects.get(user=user)
            
            cart.cart_item.all().delete()
            
            cart.total_price = 0
            cart.save()
            
            return Response({"detail": "Savat tozalandi"}, status=200)
        
        except User.DoesNotExist:
            return Response({"detail": "Foydalanuvchi topilmadi"}, status=404)
        except CartModel.DoesNotExist:
            return Response({"detail": "Savat topilmadi"}, status=404)      
        
        
    @action(detail=False, methods=["delete"], url_path='remove')
    def remove_item(self, request):
        tg_id = request.data.get("tg_id")
        product_id = request.data.get("product_id")

        if not product_id:
            return Response({"detail": "product_id kerak"}, status=400)

        try:
            user = User.objects.get(tg_id=tg_id)
            cart = CartModel.objects.get(user=user)
            
            cart_item = cart.cart_item.get(product_id=product_id)
            cart_item.delete()

            total = cart.cart_item.aggregate(total=Sum('total_price'))['total'] or 0
            cart.total_price = total
            cart.save()

            return Response({"detail": f"Product savatdan o‘chirildi"}, status=200)

        except User.DoesNotExist:
            return Response({"detail": "Foydalanuvchi topilmadi"}, status=404)
        except CartModel.DoesNotExist:
            return Response({"detail": "Savat topilmadi"}, status=404)
        except CartitemModel.DoesNotExist:
            return Response({"detail": f"Product savatda topilmadi"}, status=404)
        


@extend_schema(tags=["cartItem"])
class CartitemView(BaseViewSetMixin, ModelViewSet):
    queryset = CartitemModel.objects.all()
    serializer_class = ListCartitemSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartitemSerializer,
        "retrieve": RetrieveCartitemSerializer,
        "create": CreateCartitemSerializer,
    }
