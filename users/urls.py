from django.urls import path, include
from .views import (
    CreateUserView,
    ListUserView,
    UserLoginView,
    UserLogoutView,
    CookieTokenRefreshView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
)

urlpatterns = [
    path("auth/users", ListUserView.as_view(), name="list"),
    path("auth/register", CreateUserView.as_view(), name="register"),
    path("token", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh", CookieTokenRefreshView.as_view(), name="refresh"),
    path("auth/login", UserLoginView.as_view(), name="login"),
    path("auth/logout", UserLogoutView.as_view(), name="logout"),
    path("token/verify", TokenVerifyView.as_view(), name="verify"),
    path("auth", include("rest_framework.urls"))
]