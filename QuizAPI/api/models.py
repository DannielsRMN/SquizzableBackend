from django.db import models

# Create your models here.

# By Danniels.
# Clase que contendrá la foto de perfil del usuario
class FotoPerfil(models.Model):
    idFoto = models.AutoField(primary_key=True)
    pfp = models.ImageField(upload_to="imagenes/")

    def __str__(self):
        return f"Foto de Perfil Nro. {self.pfp}"

# Clase para manejar la información del usuario
class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50)
    puntajeTotal = models.IntegerField()
    
    def __str__(self):
        return f"Perfil de {self.nickname}"

# Clase para manejar los datos de login o permisos de administrador del usuario
class Usuario(models.Model):
    idUniqueUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    userPassword = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=False)

    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE)
    fotoPerfil = models.OneToOneField(FotoPerfil, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nombre de usuario: {self.username}"

# Clase que manejará las dificultades que manejará el software, así evitamos facil y fácil.    
class Dificultad(models.Model):
    idDificultad = models.AutoField(primary_key=True)
    nombreDiff = models.CharField(max_length=50)
    descDiff = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreDiff

# De la misma forma, manejamos los estados Capacitado, En progreso, Sin Progreso, etc.    
class EstadoFinal(models.Model):
    idEstadoFinal = models.AutoField(primary_key=True)
    nombreEstadoFinal = models.CharField(max_length=50)
    descEstadoFinal = models.CharField(max_length=250)

    def __str__(self):
        return self.nombreEstadoFinal

# By Raul.
# La especialidad de los modelos, estos pueden ser para filtrar. Ejm: Docencia, Secretaria, Mantenimiento, etc.
class Especialidad(models.Model):
    idEspecialidad=models.AutoField(primary_key=True)
    nombreEspecialidad=models.CharField(max_length=50)

    def __str__(self):
         return self.nombreEspecialidad

# Modulos completos sobre ciertas capacitaciones
class Modulo(models.Model):
    idModulo=models.AutoField(primary_key=True)
    nombreModulo=models.CharField(max_length=50)
    
    dif=models.ForeignKey(Dificultad, on_delete=models.CASCADE)
    espe=models.ForeignKey(Especialidad,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombreModulo} - {self.espe} - {self.dif}"
    
# By Edson.
# Progreso que manejará el avance de un usuario y un cierto módulo
class Progreso(models.Model):
    idProgreso = models.AutoField(primary_key=True)
    porcentajeCompletado = models.FloatField()
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    puntajeObtenido = models.IntegerField()
    
    estadoFinal = models.ForeignKey(EstadoFinal, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    modulo = models.OneToOneField(Modulo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Progreso de {self.usuario.username} en {self.modulo.nombreModulo} - {self.porcentajeCompletado}%"

# By Jean.
# Temas que se presentarán dentro de un módulo
class Tema(models.Model):
    idTema = models.AutoField(primary_key=True)
    nombreTema = models.CharField(max_length=100)
    
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTema

# Preguntas de un cierto tema
class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True) 
    pregunta = models.CharField(max_length=500) 

    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='preguntas')  
    
    def __str__(self):
        return self.pregunta if len(self.pregunta) < 50 else self.pregunta[:47] + '...' 
    
# By Jeferson.
# Alternativas de las preguntas
class Alternativa (models.Model):
    idAlternativa=models.AutoField(primary_key=True)
    alternativa=models.CharField(max_length=250)
    puntajeObtenido=models.BigIntegerField()
    
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.alternativa

# Selección de la alternativa, principalmente para evaluarlo y cuando se registró
class AlternativaSeleccionada(models.Model):
    idRespuesta=models.AutoField(primary_key=True)
    fechaRegistroRespuesta=models.DateField()

    alternativa=models.OneToOneField(Alternativa,on_delete=models.CASCADE)

    def __str__(self):
        return self.fechaRegistroRespuesta