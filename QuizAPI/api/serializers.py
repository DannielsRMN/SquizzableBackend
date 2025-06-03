from rest_framework import serializers
from . import models

class FotoPerfilSerializador(serializers.ModelSerializer):

    class Meta:
        model = models.FotoPerfil
        fields = "__all__"

class EvaluacionSerializador(serializers.ModelSerializer):
    
    class Meta:
        model = models.Evaluacion
        fields = "__all__"

class UsuarioSerializador(serializers.ModelSerializer):

    class Meta:
        model = models.Usuario
        fields = "__all__"

    def create(self, validated_data):
        user = models.Usuario(
            email = validated_data['email'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Especialidad
        fields = "__all__"


class ModuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Modulo
        fields = "__all__"

class ProgresoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Progreso
        fields = "__all__"

class TemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tema
        fields = "__all__"

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pregunta
        fields = "__all__"

class SerializadorAlternativa(serializers.ModelSerializer):

    class Meta:
        model=models.Alternativa
        fields = "__all__"

class CargoSerializador(serializers.ModelSerializer):

    class Meta:
        model=models.Cargo
        fields = '__all__'

class RespuestaSerializador(serializers.ModelSerializer):

    class Meta:
        model = models.Respuesta
        fields = '__all__'