from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("api/users", views.RegistrationView.as_view(), name="main-app"),
    path("api/token", TokenObtainPairView.as_view(), name="obtain-token"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh-token"),
]
