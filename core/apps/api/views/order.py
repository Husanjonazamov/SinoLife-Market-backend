from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import OrderitemModel, OrderModel
from core.apps.api.serializers.order import (
    CreateOrderitemSerializer,
    CreateOrderSerializer,
    ListOrderitemSerializer,
    ListOrderSerializer,
    RetrieveOrderitemSerializer,
    RetrieveOrderSerializer,
)


@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = ListOrderSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
    }
    
    def get_queryset(self):
        tg_id = self.request.query_params.get("tg_id")
        return OrderModel.objects.filter(user__tg_id=tg_id)


@extend_schema(tags=["orderItem"])
class OrderitemView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderitemModel.objects.all()
    serializer_class = ListOrderitemSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderitemSerializer,
        "retrieve": RetrieveOrderitemSerializer,
        "create": CreateOrderitemSerializer,
    }
