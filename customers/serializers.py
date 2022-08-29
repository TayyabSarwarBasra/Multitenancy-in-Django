from django.contrib.auth import validators
from pkg_resources import _
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from rest_framework.validators import UniqueValidator
import random

from customers.models import *


class ClientSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', "username", 'email', 'first_name', 'last_name', 'mobile_number', 'business_name', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            } }

    @staticmethod
    def validate_password(data):
        validators.validate_password(password=data, user=Client)
        return data

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        gallery = attrs.get("gallery")
        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': _("Your Password not matched!")})

        if Client.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError({'email': _("Sorry, user already exist with this email, "
                                                          "try with different email.")})
        if Client.objects.filter(mobile_number=attrs["mobile_number"]).exists():
            raise serializers.ValidationError({'phone': _("Sorry, user already exist with this phone, "
                                                          "try with different phone.")})

        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Client.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ('id', 'domain', 'is_primary', 'tenant')

