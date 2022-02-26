from django.urls import path
from .views import GetFeeDetailsView
urlpatterns = [
    path('fee/',GetFeeDetailsView.as_view(),name="Get fees")
]