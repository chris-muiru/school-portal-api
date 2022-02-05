from django.urls import path
from .views import GetUserCredentials


urlpatterns = [
    path('student-detail/',GetUserCredentials.as_view(),name="student-credentials")
]
