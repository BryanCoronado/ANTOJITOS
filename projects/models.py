from django.db import models

# Create your models here.

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='projects/images/')    
    
    
    
    
    def __str__(self):
        return self.nombre