from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.payme import PaymeCallBackAPIView
from .views.click import ClickWebhookAPIView
router = DefaultRouter()


urlpatterns = [
    path("", include(router.urls)),
    path("payment/update/", PaymeCallBackAPIView.as_view()),
    path("click/update/", ClickWebhookAPIView.as_view()),
]
