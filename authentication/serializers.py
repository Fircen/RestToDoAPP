from multiprocessing import AuthenticationError
from rest_framework import serializers
from .models import User
from django.contrib import auth
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length = 6, max_length = 64)
    class Meta:
        model = User
        fields = ('id', 'password', 'email',)
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.object.create(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 3)
    password = serializers.CharField(max_length = 64, min_length = 6, write_only = True)
    
    class Meta:
        model = User
        fields = ['email', 'password','tokens']

    def validate(self,attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email = email, password = password)
        if not user:
            raise AuthenticationError('Invalid credentials')
        if not user.is_active:
            raise AuthenticationError('Account disable')
        """
        if not user.is_verified:
            raise AuthenticationError('Email is not verified')
        """
        

        return{
            'email' : user.email,
            'tokens' : user.tokens(),
        }
        