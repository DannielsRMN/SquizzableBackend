from django.shortcuts import render
from rest_framework import viewsets, permissions

from . import models, serializers

# Create your views here.

# By Danniels

class FotoPerfilViewset(viewsets.ModelViewSet):
    queryset = models.FotoPerfil.objects.all()
    serializer_class = serializers.FotoPerfilSerializador

    permission_classes = [permissions.IsAuthenticated]

class PerfilViewset(viewsets.ModelViewSet):
    queryset = models.Perfil.objects.all()
    serializer_class = serializers.PerfilSerializador

    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializador

    permission_classes = [permissions.IsAuthenticated]

class DificultadViewset(viewsets.ModelViewSet):
    queryset = models.Dificultad.objects.all()
    serializer_class = serializers.DificultadSerializador

    permission_classes = [permissions.IsAuthenticated]

class EstadoFinalViewset(viewsets.ModelViewSet):
    queryset = models.EstadoFinal.objects.all()
    serializer_class = serializers.EstadoFinalSerializador

    permission_classes = [permissions.IsAuthenticated]

# By Raul.

class EspecialidadViewset(viewsets.ModelViewSet):
   queryset = models.Especialidad.objects.all()
   serializer_class = serializers.EspecialidadSerializer

   permission_classes = [permissions.IsAuthenticated]

class ModuloViewset(viewsets.ModelViewSet):
   queryset = models.Modulo.objects.all()
   serializer_class = serializers.ModuloSerializer

   permission_classes = [permissions.IsAuthenticated]

# By Edson.

class ProgresoViewset(viewsets.ModelViewSet):
    queryset = models.Progreso.objects.all()
    serializer_class = serializers.ProgresoSerializer

    permission_classes = [permissions.IsAuthenticated]

# By Jean.

class TemaViewSet(viewsets.ModelViewSet):
    queryset = models.Tema.objects.all()
    serializer_class = serializers.TemaSerializer

    permission_classes = [permissions.IsAuthenticated]

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = models.Pregunta.objects.all()
    serializer_class = serializers.PreguntaSerializer

    permission_classes = [permissions.IsAuthenticated]

# By Jeferson.

class AlternativaViewsets (viewsets.ModelViewSet):
    queryset=models.Alternativa.objects.all()
    serializer_class=serializers.SerializadorAlternativa

    permission_classes = [permissions.IsAuthenticated]

class AlternativaSeleccionaViewsets (viewsets.ModelViewSet):
    queryset=models.AlternativaSeleccionada.objects.all()
    serializer_class=serializers.SerializadorAlternativaSelecionado
    
    permission_classes = [permissions.IsAuthenticated]