from django.db import models
from cloudinary.models import CloudinaryField

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True)
    glb_url = CloudinaryField('glb_model')

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.vin})"
    
class WrapMaterial(models.Model):
    name = models.CharField(max_length=100)
    texture_url = CloudinaryField('texture_image')
    description = models.TextField()

    def __str__(self):
        return self.name
    