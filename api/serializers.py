from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Item

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'name', 'weight', 'description', 'price', 'id']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['flight', 'date', 'id']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'name', 'size', 'weight', 'price', 'description', 'id']
