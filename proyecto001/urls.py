"""
URL configuration for proyecto001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name = "inicio"),
    path('listado_paises/', views.cursos, name='cursos'),
    path('registrar_paises/', views.crear_curso, name='crear_curso'),
    path('eliminar_paises/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('listado_editorial/', views.listar_carreras, name='carreras'),
    path('registrar_editorial/', views.crear_carrera, name='crear_carrera'),
    path('eliminar_editorial/<int:carrera_id>/', views.eliminar_carrera, name='eliminar_carrera'),
    path('editar_editorial/<int:carrera_id>/', views.editar_carrera, name='editar_carrera'),
    path('integrantes/',views.integrantes, name = "integrantes"),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)