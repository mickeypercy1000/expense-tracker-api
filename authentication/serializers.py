import re
from user.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from authentication import validators
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError


class CreateUserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField(
        max_length=100, required=True, validators=[validators.EmailValidation],
        error_messages={
            'invalid': 'Please provide a valid email address',
            'blank': 'Please provide a valid email address',
            'required': 'Please provide a valid email address',
            })
    username = serializers.CharField(
        max_length=100, required=True, validators=[validators.UsernameValidation],
        error_messages={
            'blank': 'Please provide a username',
            'required': 'Please provide a username',
            })
    firstname = serializers.CharField(max_length=100, required=False, allow_blank=True, validators=[validators.FirstnameValidation])
    lastname = serializers.CharField(max_length=100, required=False, allow_blank=True, validators=[validators.LastnameValidation])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ["id", "email", "firstname", "lastname", "username", "password"]

    def create(self, validated_data):
        print(validated_data)
        validated_data.get("email").lower()  # convert email to lowercase
        validated_data.get("firstname", "").capitalize()  # convert first letter to capital
        validated_data.get("lastname", "").capitalize()  # convert first letter to capital
        user = User.objects.create(**validated_data)
        print("User created", user)
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        error_messages={
            'blank': 'Email is required',
            'required': 'Email is required',
            })
    password = serializers.CharField(
        error_messages={
            'blank': 'Password is required',
            'required': 'Password is required',
            })

    class Meta:
        model = User
        fields = ["email", "password"]

    def validate(self, data):
        print("my data", data)

        email = data.get('email')
        password = data.get('password')
        user = authenticate(email=email, password=password)
        if not user:
            message = {"login_error": "Email or password is incorrect"}
            raise serializers.ValidationError(message)
        data['user'] = user
        return data




class LogoutUserSerializer(serializers.ModelSerializer):

    refresh = serializers.CharField()

    class Meta:
        model = User
        fields = ['refresh', ]
        
    def validate(self, attrs):
        try:
            token = RefreshToken(attrs['refresh'])
            token.blacklist()
        except TokenError:
            raise ValidationError({'message': 'Invalid refresh token'})
        return {}


class UpdateRetrieveUserSerializer(serializers.ModelSerializer):
    """
    Update user profile,
    Retrieve user detail,
    """
    id = serializers.CharField(read_only=True)
    firstname = serializers.CharField(max_length=100, required=False, allow_blank=True, validators=[validators.FirstnameValidation])
    lastname = serializers.CharField(max_length=100, required=False, allow_blank=True, validators=[validators.LastnameValidation])
    username = serializers.CharField(
        max_length=100, required=False,
        error_messages={
            'blank': 'Please provide a username',
            })

    class Meta:
        model = User
        fields = ["id", "firstname", "lastname", "username", "email"]

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get("firstname", instance.firstname)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.username = validated_data.get('username', instance.username)

        instance.save()
        return instance

    def get(self, validated_data):
        print("data", validated_data)
