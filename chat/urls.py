# your_app_name/urls.py
from django.urls import path
from .views import CuisineList, CuisineDetail, RecipeListCreate, RecipeDetail

from rest_framework.authtoken.views import obtain_auth_token
from .views import UserCreate

urlpatterns = [
    path('cuisines/', CuisineList.as_view(), name='cuisine-list'),
    path('cuisines/<int:pk>/', CuisineDetail.as_view(), name='cuisine-detail'),
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('register/', UserCreate.as_view(), name='user-create'),  # User registration
    path('login/', obtain_auth_token, name='api_token_auth'),  # Login to get token
]
