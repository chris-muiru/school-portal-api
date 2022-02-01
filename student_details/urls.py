from django.urls import path
from .views import GetUserCredentials


urlpatterns = [
    path('student-details/',GetUserCredentials.as_view(),name="student-credentials")
]
