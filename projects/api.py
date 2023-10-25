from projects.models import Proyecto
from rest_framework import viewsets, permissions
from .serializer import ProyectoSerializer

class ProjectViewSet(viewsets.ModelViewSet):
  queryset = Proyecto.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ProyectoSerializer