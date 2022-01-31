from django.urls import path,include
from . import views 

urlpatterns = [
    path('results/',views.Student_result.as_view())
]