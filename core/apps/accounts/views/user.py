from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from core.apps.accounts.serializers.user import UserUpdateBotSerializer
from rest_framework.permissions import AllowAny

from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
User = get_user_model()



class UserViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserUpdateBotSerializer
    permission_classes = [AllowAny]
    lookup_field = 'tg_id'  

    @action(detail=True, methods=['patch'], url_path='update-info')
    def update_info(self, request, tg_id=None):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)