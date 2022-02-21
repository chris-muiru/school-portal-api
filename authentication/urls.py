from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('api/token/',TokenObtainPairView.as_view(),name="token-obtain-pair"), 
    path('api/token/refresh/',TokenRefreshView.as_view(),name="autoken-refresh") 
]

