from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views

# Imagenes
from django.conf import settings
from django.conf.urls.static import static

# By Danniels
router = DefaultRouter()
router.register(r'FotoPerfil', views.FotoPerfilViewset)
router.register(r'Perfil', views.PerfilViewset)
router.register(r'Usuario', views.UsuarioViewset)
router.register(r'Dificultad', views.DificultadViewset)
router.register(r'EstadoFinal', views.EstadoFinalViewset)

# By Raul.
router.register('Especialidad',views.EspecialidadViewset)
router.register('Modulo',views.ModuloViewset)

# By Edson.
router.register('Progreso', views.ProgresoViewset)

# By Jean.
router.register('Temas', views.TemaViewSet)
router.register('Preguntas', views.PreguntaViewSet)

# By Jeferson.
router.register(r"Alternativa",views.AlternativaViewsets)
router.register(r"AlternativaSeleccionada",views.AlternativaSeleccionaViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
