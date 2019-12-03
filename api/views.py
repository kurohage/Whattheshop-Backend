from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Product, Item, Order, Profile
from .serializers import UserCreateSerializer, ProductSerializer, OrderSerializer, ProfileSerializer
from .permissions import IsOrderOwner

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class ProductsList(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class OrdersList(ListAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated, IsOrderOwner]

	def get_queryset(self):
		return Order.objects.filter(profile__user=self.request.user)

class ProfileDetail(ListAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Profile.objects.filter(user=self.request.user)