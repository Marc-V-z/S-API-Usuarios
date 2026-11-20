from rest_framework import generics
from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.order_by('id')
    serializer_class = UsuarioSerializer