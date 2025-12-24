
from rest_framework import serializers
from .models import Vehicle, WrapMaterial

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__' #['id', 'make', 'model', 'year', 'color', 'vin', glb_url]
class WrapMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = WrapMaterial
        fields = '__all__' #['id', 'name', 'texture_url', 'description']
