from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views


urlpatterns = [
    path('products/', views.ProductsList.as_view(), name='products-list'),
    #path('products/<int:product_id>/', views.ProductDetails.as_view(), name='product-details'),

    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('register/', views.UserCreateAPIView.as_view(), name="register"),
    
]