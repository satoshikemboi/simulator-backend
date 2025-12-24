
from django.urls import path
from .views import VehicleListView, MaterialListView

urlpatterns = [
    path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('materials/', MaterialListView.as_view(), name='material-list'),
]