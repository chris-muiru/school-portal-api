from .views import RegisterUser
from rest_framework.authtoken import views
from django.urls import path
urlpatterns=[
    path('register/',RegisterUser.as_view(),name="register-user"),
    path('api-token-auth/',views.obtain_auth_token) 
]