from django.urls import path
from . import views

# Lista de URL patterns (rutas) para las vistas de visitas
urlpatterns = [
    # Ruta para mostrar la lista de visitas
    path("", views.lista_visitas, name="lista_visitas"),

    # Ruta para registrar una nueva visita
    path("visita/registrar/", views.registrar_visita, name="registrar_visita"),

    # Ruta para editar una visita existente (con parámetro 'rut' en la URL)
    path("visita/editar/<str:rut>/", views.editar_visita, name="editar_visita"),

    # Ruta para eliminar una visita (con parámetro 'rut' en la URL)
    path("visita/eliminar/<str:rut>/", views.eliminar_visita, name="eliminar_visita"),
]
