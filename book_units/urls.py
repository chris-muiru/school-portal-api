from django.urls import path
from . import views
urlpatterns=[
    path('units/',views.Get_Units.as_view()),
    path('book/',views.Set_selected_units.as_view()),
    path('selected/',views.GetSelectedUnits.as_view(),name='booked-units')
]

