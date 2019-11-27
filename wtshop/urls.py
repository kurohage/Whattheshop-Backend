from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('register/', views.UserCreateAPIView.as_view(), name="register"),
]


if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)