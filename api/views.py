from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, ProductSerializer

from rest_framework.response import Response
from .models import Product, Item

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ProductsList(ListAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer