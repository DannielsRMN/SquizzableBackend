from rest_framework import serializers
from . import models

# By Danniels

class FotoPerfilSerializador(serializers.ModelSerializer):
    class Meta:
        model = models.FotoPerfil
        fields = "__all__"

class PerfilSerializador(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil
        fields = "__all__"

class UsuarioSerializador(serializers.ModelSerializer):

    Perfil_nombre = serializers.ReadOnlyField(source='perfil.nickname')
    FotoPerfil_id = serializers.ReadOnlyField(source='fotoPerfil.idFoto')

    class Meta:
        model = models.Usuario
        fields = "__all__"

class DificultadSerializador(serializers.ModelSerializer):
    class Meta:
        model = models.Dificultad
        fields = "__all__"

class EstadoFinalSerializador(serializers.ModelSerializer):
    class Meta:
        model = models.EstadoFinal
        fields = "__all__"

# By Raul.

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Especialidad
        fields = "__all__"


class ModuloSerializer(serializers.ModelSerializer):

    especialidad = serializers.ReadOnlyField(source='especialidad.nombreEspecialidad')

    class Meta:
        model = models.Modulo
        fields = "__all__"

# By Edson.

class ProgresoSerializer(serializers.ModelSerializer):

    nombreModulo = serializers.ReadOnlyField(source='modulo.nombreModulo')
    nombreUsuario = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = models.Progreso
        fields = "__all__"

# By Jean.

class TemaSerializer(serializers.ModelSerializer):

    nombreModulo = serializers.ReadOnlyField(source='modulo.nombreModulo')

    class Meta:
        model = models.Tema
        fields = "__all__"

class PreguntaSerializer(serializers.ModelSerializer):

    nombreTema = serializers.ReadOnlyField(source='tema.nombreTema')

    class Meta:
        model = models.Pregunta
        fields = "__all__"

# By Jeferson.

class SerializadorAlternativa(serializers.ModelSerializer):

    preguntaText = serializers.ReadOnlyField(source='pregunta.pregunta')

    class Meta:
        model=models.Alternativa
        fields = "__all__"

class SerializadorAlternativaSelecionado(serializers.ModelSerializer):

    alternativaSelec = serializers.ReadOnlyField(source='alternativa.alternativa')

    class Meta:
        model=models.AlternativaSeleccionada
        fields = "__all__"
        