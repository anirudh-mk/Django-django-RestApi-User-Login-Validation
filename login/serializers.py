from rest_framework import serializers


class LoginSerializers(serializers.Serializer):
    user = serializers.CharField()
    password = serializers.CharField()
