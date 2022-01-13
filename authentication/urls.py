from django.urls import path
from .views import register_user
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('register/',register_user.as_view(),name="register"),
    path('login/',obtain_auth_token,name="login")
]