from rest_framework import serializers
from core.models import ToDo


class AuthSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)
    company_id = serializers.IntegerField(required=True)
