"""Provide serializer for application objects."""
from django.contrib.auth.models import User
from .models import QueryLog
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Define a serializer for the User Model."""

    class Meta:
        """Defines Metadata for User Serializer."""

        model = User
        fields = ("id", "username", "password", "email", "first_name", "last_name")
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        """Overloads the create method to get custom user creation."""
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class QueryLogSerializer(serializers.ModelSerializer):
    """Define a serializer for the Query Log Model."""

    class Meta:
        """Defines Metadata for Query Log Serializer."""

        model = QueryLog
        fields = ("id", "query_string", "created_at")
        read_only_fields = ("id",)

    def create(self, validated_data):
        pass
