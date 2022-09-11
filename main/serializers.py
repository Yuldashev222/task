from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Journal, User, WashCompany
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Register serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','name', 'role')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,name=validated_data['name'],  role=validated_data['role'])
        return user
    
    
# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
# WashCompany serializer
class WashCompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WashCompany
        fields = '__all__'
        
        
class JournalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Journal
        fields = '__all__'
        
        
