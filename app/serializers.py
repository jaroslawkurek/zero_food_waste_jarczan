from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import Account
from .tokens import validate_token


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "email", "display_name", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """
        Create and return a new "Account" instance.
        """
        return Account.objects.create_user(**validated_data)

    def validate_password(self, value):
        validate_password(value)
        return value


class TokenSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    token = serializers.CharField()

    def validate(self, data):
        try:
            user = Account.objects.get(id=data["id"])
        except Account.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid user id or user doesn't exist."})
        is_token_valid = validate_token(user, data["token"])
        if is_token_valid or user.is_active:
            return data
        else:
            raise serializers.ValidationError({"message": "Token has expired or invalid."})
