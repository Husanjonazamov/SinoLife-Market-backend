from django.contrib.auth import get_user_model
from rest_framework import serializers



User = get_user_model()

class UserUpdateBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['tg_id', 'first_name', 'phone', 'lang']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = [
            "created_at",
            "updated_at",
            "password",
            "groups",
            "user_permissions"
        ]
        model = get_user_model()


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name"
        ]
