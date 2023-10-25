from rest_framework import serializers


from  .models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('id', 'nombre', 'descripcion', 'tipo', 'cantidad', 'precio', 'imagen')