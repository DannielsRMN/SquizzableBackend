from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from api import views

# Imagenes
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'FotoPerfil', views.FotoPerfilViewset)
router.register(r'Usuario', views.UsuarioViewset)
router.register(r'Evaluacion', views.EvaluacionViewsets)
router.register(r'Respuesta', views.RespuestaViewsets)

router.register('Especialidad',views.EspecialidadViewset)
router.register('Modulo',views.ModuloViewset)

router.register('Progreso', views.ProgresoViewset)

router.register('Temas', views.TemaViewSet)
router.register('Preguntas', views.PreguntaViewSet)

router.register(r"Alternativa",views.AlternativaViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('api/token-auth/', views.CustomAuthToken.as_view(),name='token-auth'),
    path('api/modulos/<int:especialidadID>/', views.ModulosPersonales.as_view(), name='modulos-personales'),
    path('api/clasificacion/', views.ClasificacionUsuario.as_view(), name='clasificacion-usuario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
