from django.urls import path
from authapi.views import LoginUser, RegisterUser, ChangePassword, UpdateProfile, DeleteAccount
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('', views.api_routes),
    path('users/', views.get_all_users),
    path('users/<int:pk>/', views.get_users_by_id),
    path('login/', LoginUser.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('signup/', RegisterUser.as_view(), name='register'),
    path('change-password/<int:pk>/', ChangePassword.as_view(), name='change_password'),
    path('update-profile/<int:pk>/', UpdateProfile.as_view(), name='change_password'),
    path('delete/<int:pk>/', DeleteAccount.as_view(), name='delete'),
    path('delete-all/', views.delete_all_users, name='delete-all'),

]
