from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('activation/', views.ActivationView.as_view()),
    path('users/', views.UserListAPIView.as_view()),
    path('users/profile/<int:pk>/', views.ProfileRetrieveAPIView.as_view()),
    path('users/update/<int:pk>/', views.ProfileUpdateAPIView.as_view()),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

