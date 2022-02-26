from django.urls import path
from . import views
urlpatterns=[
    path('units/',views.Get_Units.as_view()),
    path('book-units/',views.SetSelectedUnits.as_view()),
    path('selected-units/',views.GetSelectedUnits.as_view())
]

