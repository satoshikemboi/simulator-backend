from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Vehicle, WrapMaterial
from .serializers import VehicleSerializer, WrapMaterialSerializer

class VehicleListView(generics.ListAPIView):
        # Return a list of all available 3D car models
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class MaterialListView(generics.ListAPIView):
        # Return a list of all available wrap materials/colors
    queryset = WrapMaterial.objects.all()
    serializer_class = WrapMaterialSerializer