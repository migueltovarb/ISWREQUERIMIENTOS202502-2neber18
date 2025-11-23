from django.urls import path
from .views import salas_list, salas_crear, salas_editar, salas_eliminar

urlpatterns = [
    path('', salas_list, name='salas_list'),
    path('crear/', salas_crear, name='salas_crear'),
    path('editar/<int:id>/', salas_editar, name='salas_editar'),
    path('eliminar/<int:id>/', salas_eliminar, name='salas_eliminar'),
]
