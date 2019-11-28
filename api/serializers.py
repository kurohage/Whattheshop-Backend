from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Item

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image_url', 'name', 'price', 'id']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['flight', 'date', 'id']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image_url', 'name', 'size', 'weight', 'price', 'description', 'id']
