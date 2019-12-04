from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Product, Item, Order, Profile
from .serializers import (
	ProductSerializer,
	OrderSerializer,
	ProfileSerializer,
	ProfileCreateSerializer,
	TokenObtainPairWithProfileSerializer)
from .permissions import IsOrderOwner

class ProfileCreateAPIView(CreateAPIView):
    serializer_class = ProfileCreateSerializer
    permission_classes = [AllowAny]

class ProductsList(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class OrdersList(ListAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated, IsOrderOwner]

	def get_queryset(self):
		return Order.objects.filter(profile__user=self.request.user)

class ProfileDetail(RetrieveAPIView):
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return Profile.objects.get(user=self.request.user)

class TokenObtainPairWithProfileView(TokenObtainPairView):
	serializer_class = TokenObtainPairWithProfileSerializer