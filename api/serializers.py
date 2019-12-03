from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Item, Order, Profile

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

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User    
        fields = ['first_name', 'last_name', 'username', 'id']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'name', 'weight', 'description', 'price', 'id']


class ItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer() # this returns full product object, which isn't needed
    #product = serializers.SlugRelatedField(
    #        read_only=True,
    #        slug_field='name'
    #    )

    class Meta:
        model = Item
        fields = ['product', 'order', 'quantity', 'price', 'id']


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    #items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True) # this returned the item's ID, which is bad as we'd need to do yet another query

    class Meta:
        model = Order
        fields = ['items', 'date', 'id']

    def get_items(self, object):
        items = Item.objects.filter(order=object.id)
        serializer = ItemSerializer(instance=items, many=True)
        return serializer.data


class ProfileSerializer(serializers.ModelSerializer):

    user = UserInfoSerializer()
    orders = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ['user', 'email', 'orders']

    def get_orders(self, object):
        # answer found here: https://stackoverflow.com/questions/25312987/django-rest-framework-limited-queryset-for-nested-modelserializer
        orders = Order.objects.filter(profile__user=object.user)
        serializer = OrderSerializer(instance=orders, many=True)
        return serializer.data