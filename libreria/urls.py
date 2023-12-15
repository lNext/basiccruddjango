from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("equipo", views.equipo, name="equipo"),
    path("contacto", views.contacto, name="contacto"),
    path("enviar_correo", views.enviar_correo, name="enviar_correo"),
    path("libros", views.libros, name="libros"),
    path("libros/crear", views.crearLibro, name="crearLibro"),
    path("libros/editar/<int:id>", views.editar, name="editar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
