from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Cargo(models.Model):
    idCargo = models.AutoField(primary_key=True)
    nombreCargo = models.CharField(max_length=50)

class UsuarioManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        if not email:
            raise ValueError('Correo es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El campo staff debe ser True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El campo superusuario debe ser True')
        
        return self.create_user(username,email,password,**extra_fields)

class Usuario(AbstractUser):

    objects = UsuarioManager()

    idUsuario = models.AutoField(primary_key=True)
    fechaContratacion = models.DateField(null=True ,blank=True)
    puntos = models.IntegerField(default=0)

    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True ,blank=True)

class FotoPerfil(models.Model):
    idFoto = models.AutoField(primary_key=True)
    pfp = models.ImageField(upload_to="usuarios/")
    
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Especialidad(models.Model):
    idEspecialidad=models.AutoField(primary_key=True)
    nombreEspecialidad=models.CharField(max_length=50)

class Modulo(models.Model):
    idModulo=models.AutoField(primary_key=True)
    nombreModulo=models.CharField(max_length=50)
    dificultad=models.CharField(max_length=50)

    especialidad=models.ForeignKey(Especialidad,on_delete=models.CASCADE)
    
class Tema(models.Model):
    idTema = models.AutoField(primary_key=True)
    nombreTema = models.CharField(max_length=100)
    contenido = models.TextField()
    puntosTotal = models.IntegerField(default=0)
    
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)

class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True) 
    pregunta = models.CharField(max_length=500)

    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='preguntas')  
    
class Alternativa (models.Model):
    idAlternativa=models.AutoField(primary_key=True)
    alternativa=models.CharField(max_length=250)
    esCorrecta = models.BooleanField(default=False)
    
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)

class Evaluacion(models.Model):
    idEvaluacion=models.AutoField(primary_key=True)
    multiplicador = models.FloatField(default=0)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pregunta = models.ManyToManyField(Pregunta)

class Respuesta(models.Model):
    idRespuesta = models.AutoField(primary_key=True)

    alternativa = models.ManyToManyField(Alternativa)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)

class Progreso(models.Model):
    idProgreso = models.AutoField(primary_key=True)
    fechaInicio = models.DateField(auto_now_add=True)
    fechaFin = models.DateField(null=True)
    ronda = models.IntegerField(default=1)
    
    evaluacion = models.OneToOneField(Evaluacion, on_delete=models.CASCADE)