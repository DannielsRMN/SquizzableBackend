from django.shortcuts import render
from rest_framework import viewsets, permissions

from rest_framework import response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


from . import models, serializers

# Create your views here.

class FotoPerfilViewset(viewsets.ModelViewSet):
    queryset = models.FotoPerfil.objects.all()
    serializer_class = serializers.FotoPerfilSerializador

    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializador

    permission_classes = [permissions.IsAuthenticated]

class EspecialidadViewset(viewsets.ModelViewSet):
   queryset = models.Especialidad.objects.all()
   serializer_class = serializers.EspecialidadSerializer

   permission_classes = [permissions.IsAuthenticated]

class ModuloViewset(viewsets.ModelViewSet):
   queryset = models.Modulo.objects.all()
   serializer_class = serializers.ModuloSerializer

   permission_classes = [permissions.IsAuthenticated]

class ProgresoViewset(viewsets.ModelViewSet):
    queryset = models.Progreso.objects.all()
    serializer_class = serializers.ProgresoSerializer

    permission_classes = [permissions.IsAuthenticated]

class TemaViewSet(viewsets.ModelViewSet):
    queryset = models.Tema.objects.all()
    serializer_class = serializers.TemaSerializer

    permission_classes = [permissions.IsAuthenticated]

class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = models.Pregunta.objects.all()
    serializer_class = serializers.PreguntaSerializer

    permission_classes = [permissions.IsAuthenticated]

class AlternativaViewsets (viewsets.ModelViewSet):
    queryset=models.Alternativa.objects.all()
    serializer_class=serializers.SerializadorAlternativa

    permission_classes = [permissions.IsAuthenticated]

class EvaluacionViewsets (viewsets.ModelViewSet):
    queryset=models.Evaluacion.objects.all()
    serializer_class=serializers.EvaluacionSerializador

    permission_classes = [permissions.IsAuthenticated]

class CargoViewsets (viewsets.ModelViewSet):
    queryset = models.Cargo.objects.all()
    serializer_class=serializers.CargoSerializador

    permission_classes = [permissions.IsAuthenticated]

class RespuestaViewsets (viewsets.ModelViewSet):
    queryset = models.Respuesta.objects.all()
    serializer_class = serializers.RespuestaSerializador

    permission_classes = [permissions.IsAuthenticated]

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })