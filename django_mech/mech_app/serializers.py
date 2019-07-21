from rest_framework import serializers
from .models import ServiceRequest
from django.contrib.auth.models import User

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user