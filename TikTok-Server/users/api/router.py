from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from users.api.view import RegisterView, UserApiViewSet, UserMeView

router_user = DefaultRouter()

router_user.register(prefix='users', basename='users', viewset=UserApiViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/me/', UserMeView.as_view()),

]
