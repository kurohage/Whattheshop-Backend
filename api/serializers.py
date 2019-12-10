from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Product, Item, Order, Profile

# Create Profile.
# Since Profile model has User object, we'll first create a User object, then feed it to the Profile.
class ProfileCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True) # Ensure field's used when updating or creating an instance, 
    # but is not included when serializing the representation.
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True, allow_blank=False)  # Kept here temporarily.
    # Will move this later inside the user, then add Age/Gender or others.

    class Meta:
        model = Profile
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

    def create(self, validated_data):
        # First, instantiate a new user object and save it.
        username = validated_data.get("username").lower()
        password = validated_data.get("password")
        first_name = validated_data.get("first_name").title()
        last_name = validated_data.get("last_name").title()
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()

        # Second, feed the user object to Profile and give it rest of fields (email, gender, age, ...etc.)
        Profile.objects.create(user=new_user, email=validated_data.get("email").lower())
        return validated_data


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User    
        fields = ['first_name', 'last_name', 'username', 'id']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['image', 'image3d', 'name', 'weight', 'description', 'price', 'id']


class ItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer() # This returns full product object, which isn't needed.

    class Meta:
        model = Item
        fields = ['product', 'order', 'quantity', 'price', 'id']


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['product', 'quantity', 'price']


class OrderCreateSerializer(serializers.ModelSerializer):
    items = ItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items']

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            Item.objects.create(order=order, **item)
        return order


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['items', 'date', 'id']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    orders = serializers.SerializerMethodField()
    
    class Meta:
        model = Profile
        fields = ['user', 'image', 'email', 'orders']

    def get_orders(self, object):
        # Answer found here: https://stackoverflow.com/questions/25312987/django-rest-framework-limited-queryset-for-nested-modelserializer
        orders = Order.objects.filter(profile__user=object.user).order_by("-date")
        serializer = OrderSerializer(instance=orders, many=True)
        return serializer.data


class TokenObtainPairWithProfileSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims.
        profile = Profile.objects.get(user__id=user.id)
        serializer = ProfileSerializer(instance=profile).data
        token['profile'] = serializer

        return token