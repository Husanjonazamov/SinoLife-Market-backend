from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ProductModel
from core.apps.api.serializers.product import CreateProductSerializer, ListProductSerializer, RetrieveProductSerializer


@extend_schema(tags=["product"])
class ProductView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProductSerializer,
        "retrieve": RetrieveProductSerializer,
        "create": CreateProductSerializer,
    }
