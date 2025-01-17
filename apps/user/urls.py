from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Login and JWT token generation
    path('login/', LoginView.as_view(), name='login'),
    
    # Register user
    path('register/', RegisterView.as_view(), name='register'),

    # Token Obtain and Refresh Views
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]