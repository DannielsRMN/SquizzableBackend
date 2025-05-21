from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers

# Create your views here.

# By Danniels

class FotoPerfilViewset(viewsets.ModelViewSet):
    queryset = models.FotoPerfil.objects.all()
    serializer_class = serializers.FotoPerfilSerializador

class PerfilViewset(viewsets.ModelViewSet):
    queryset = models.Perfil.objects.all()
    serializer_class = serializers.PerfilSerializador

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializador

class DificultadViewset(viewsets.ModelViewSet):
    queryset = models.Dificultad.objects.all()
    serializer_class = serializers.DificultadSerializador

class EstadoFinalViewset(viewsets.ModelViewSet):
    queryset = models.EstadoFinal.objects.all()
    serializer_class = serializers.EstadoFinalSerializador

# By Raul.

class EspecialidadViewset(viewsets.ModelViewSet):
   queryset = models.Especialidad.objects.all()
   serializer_class = serializers.EspecialidadSerializer

class ModuloViewset(viewsets.ModelViewSet):
   queryset = models.Modulo.objects.all()
   serializer_class = serializers.ModuloSerializer

# By Edson.

class ProgresoViewset(viewsets.ModelViewSet):
    queryset = models.Progreso.objects.all()
    serializer_class = serializers.ProgresoSerializer

# By Jean.

class TemaViewSet(viewsets.ModelViewSet):
    queryset = models.Tema.objects.all()
    serializer_class = serializers.TemaSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = models.Pregunta.objects.all()
    serializer_class = serializers.PreguntaSerializer

# By Jeferson.

class AlternativaViewsets (viewsets.ModelViewSet):
    queryset=models.Alternativa.objects.all()
    serializer_class=serializers.SerializadorAlternativa

class AlternativaSeleccionaViewsets (viewsets.ModelViewSet):
    queryset=models.AlternativaSeleccionada.objects.all()
    serializer_class=serializers.SerializadorAlternativaSelecionado