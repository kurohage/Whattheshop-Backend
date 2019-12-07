from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views


urlpatterns = [
    path('products/', views.ProductsList.as_view(), name='products-list'),
    #path('products/<int:product_id>/', views.ProductDetails.as_view(), name='product-details'),
    path('order_create/', views.OrderCreateAPIView.as_view(), name="order-create"),
    path('orders/', views.OrdersList.as_view(), name="orders-list"),

    path('profile/', views.ProfileDetail.as_view(), name="profile-details"),

    #path('login/', TokenObtainPairView.as_view(), name="login"),
    path('login/', views.TokenObtainPairWithProfileView.as_view(), name="login"),
    path('register/', views.ProfileCreateAPIView.as_view(), name="register"),
    
]