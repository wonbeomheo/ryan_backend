from django.urls import path, include
from .views import (
    CreateUserView,
    ListUserView,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", ListUserView.as_view(), name="list"),
    path("user/register/", CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("auth/", include("rest_framework.urls"))
]