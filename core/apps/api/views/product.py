from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ProductModel, CategoryModel
from core.apps.api.serializers.product import CreateProductSerializer, ListProductSerializer, RetrieveProductSerializer
from rest_framework.exceptions import NotFound


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

    def get_queryset(self):
        queryset = super().get_queryset()
        category_title = self.request.query_params.get("category")
        
        if category_title:
            try:
                category = CategoryModel.objects.get(title=category_title)
            except CategoryModel.DoesNotExist:
                raise NotFound("bunday category topilmadi")
            
            queryset = queryset.filter(category=category)
            
        return queryset
        
