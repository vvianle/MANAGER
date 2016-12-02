# -*- coding: utf-8 -*-
__author__ = 'TOANTV'
from rest_framework import serializers
from accounts.models import MyUser

# Class for admin gets, create user
class OneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'id', 'username', 'password', 'email', 'fullname', 'is_active', 'date_joined', "last_login", 'is_admin', 'has_working_schedule')
        read_only_fields = ('date_joined', 'last_login', 'id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Class for admin get, update and delete user information
class OneUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'id', 'username', 'email', 'fullname', 'is_active', 'date_joined', "last_login", 'is_admin', 'has_working_schedule')
        read_only_fields = ('date_joined', 'last_login', 'id')
        extra_kwargs = {'password': {'write_only': True}}


# Serializer for authenticated user
class OneAuthenticatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'fullname', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login', 'id')

# Serializer for set password
class ChangePasswordUserSerializer(serializers.Serializer):
    #password = serializers.RegexField(min_length=6, max_length=128,
                                      #regex='^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d\~\`\!\@\#\$%\^\&\*\(\)\+\-\_\=\,\;\'\"\[\]\?\<\>\\\.\/\:\{\}\|]{8,}')
    password = serializers.CharField(max_length=128)

    class Meta:
        fields = ('password')
        extra_kwargs = {'password': {'write_only': True}}

