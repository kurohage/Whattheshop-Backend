from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views


urlpatterns = [
    path('products/', views.ProductsList.as_view(), name='products-list'),
    #path('products/<int:product_id>/', views.ProductDetails.as_view(), name='product-details'),
    path('orders/', views.OrdersList.as_view(), name="order-list"),

    path('profile/', views.ProfileDetail.as_view(), name="profile-detail"),

    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('register/', views.ProfileCreateAPIView.as_view(), name="register"),
    
]