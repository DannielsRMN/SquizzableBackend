from rest_framework import serializers
from . import models

class FotoPerfilSerializador(serializers.ModelSerializer):

    usuario_ref = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = models.FotoPerfil
        fields = "__all__"

class EvaluacionSerializador(serializers.ModelSerializer):
    
    class Meta:
        model = models.Evaluacion
        fields = "__all__"

class UsuarioSerializador(serializers.ModelSerializer):

    encargado = serializers.ReadOnlyField(source='especialidad.nombreEspecialidad')

    class Meta:
        model = models.Usuario
        fields = "__all__"

    def create(self, validated_data):
        user = models.Usuario(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user 

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Especialidad
        fields = "__all__"


class ModuloSerializer(serializers.ModelSerializer):

    nombreEspecialidad = serializers.ReadOnlyField(source='especialidad.nombreEspecialidad')

    class Meta:
        model = models.Modulo
        fields = "__all__"

class ProgresoSerializer(serializers.ModelSerializer):

    usuario_ref = serializers.ReadOnlyField(source='evaluacion.usuario.idUsuario')
    user_name = serializers.ReadOnlyField(source='evaluacion.usuario.NombreUsuario')

    tema_nombre = serializers.ReadOnlyField(source='evaluacion.pregunta.tema.nombreTema')

    class Meta:
        model = models.Progreso
        fields = "__all__"

class TemaSerializer(serializers.ModelSerializer):

    nombreModulo = serializers.ReadOnlyField(source='modulo.nombreModulo')
    class Meta:
        model = models.Tema
        fields = "__all__"

class PreguntaSerializer(serializers.ModelSerializer):
    
    tema_nombre = serializers.ReadOnlyField(source='tema.nombreTema')
    class Meta:
        model = models.Pregunta
        fields = "__all__"

class SerializadorAlternativa(serializers.ModelSerializer):

    pregunta_ref = serializers.ReadOnlyField(source='pregunta.pregunta')

    class Meta:
        model=models.Alternativa
        fields = "__all__"

class RespuestaSerializador(serializers.ModelSerializer):

    class Meta:
        model = models.Respuesta
        fields = '__all__'