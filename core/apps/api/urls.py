from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import ProductView, CategoryView

router = DefaultRouter()
router.register(r"product", ProductView, basename="product")
router.register(r"category", CategoryView, basename="category")


urlpatterns = [
    path("", include(router.urls)),
]
