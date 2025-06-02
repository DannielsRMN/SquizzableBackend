from django.db import models
from django.contrib.auth.models import AbstractUser

# Clase para manejar los roles en la empresa
class Cargo(models.Model):
    idCargo = models.AutoField(primary_key=True)
    nombreCargo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCargo

# Clase para manejar los datos de login o permisos de administrador del usuario
class Usuario(AbstractUser):
    idUsuario = models.AutoField(primary_key=True)
    fechaContratacion = models.DateField(null=True ,blank=True)

    # un usuario puede tener un cargo o rol en la empresa, pero un cargo puede aparecer en muchos usuarios.
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True ,blank=True)

# Clase que contendrá la foto de perfil del usuario
class FotoPerfil(models.Model):
    idFoto = models.AutoField(primary_key=True)
    pfp = models.ImageField(upload_to="usuarios/")
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Foto de Perfil Nro. {self.pfp}"

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
    dificultad=models.CharField(max_length=50)

    especialidad=models.ForeignKey(Especialidad,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombreModulo} - {self.espe}"
    
# Evaluacion que realiza un usuario respecto a un modulo

class Evaluacion(models.Model):
    idEvaluacion=models.AutoField(primary_key=True)

    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
# Progreso que manejará el avance de un usuario y un cierto módulo
class Progreso(models.Model):
    idProgreso = models.AutoField(primary_key=True)
    fechaInicio = models.DateField(auto_now_add=True)
    fechaFin = models.DateField(null=True)
    ronda = models.IntegerField(default=1)
    
    evaluacion = models.OneToOneField(Evaluacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Progreso de {self.usuario.username} en {self.modulo.nombreModulo} - {self.porcentajeCompletado}%"

# Temas que se presentarán dentro de un módulo
class Tema(models.Model):
    idTema = models.AutoField(primary_key=True)
    nombreTema = models.CharField(max_length=100)
    contenido = models.TextField()
    
    # Uno o Muchos temas estarán integrados en un módulo
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTema

# Preguntas de un cierto tema
class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True) 
    pregunta = models.CharField(max_length=500) 

    # Una o Muchas preguntas estarán integradas en un tema
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='preguntas')  
    
    def __str__(self):
        return self.pregunta if len(self.pregunta) < 50 else self.pregunta[:47] + '...' 
    
# Alternativas de las preguntas
class Alternativa (models.Model):
    idAlternativa=models.AutoField(primary_key=True)
    alternativa=models.CharField(max_length=250)
    esCorrecta = models.BooleanField(default=False)
    
    # Las preguntas tendrán varias alternativas.
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.alternativa
