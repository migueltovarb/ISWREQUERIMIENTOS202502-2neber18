from django.urls import path
from django.shortcuts import render
from .views import (
    home, login_view, logout_view, register_view,
    dashboard,
    salas_list, salas_crear, salas_editar, salas_eliminar
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),

    # SALAS
    path('salas/', salas_list, name='salas_list'),
    path('salas/crear/', salas_crear, name='salas_crear'),
    path('salas/editar/<int:sala_id>/', salas_editar, name='salas_editar'),
    path('salas/eliminar/<int:sala_id>/', salas_eliminar, name='salas_eliminar'),

    # STYLE TILE (para pantallazo del punto 3)
    path('style-tile/', lambda request: render(request, 'style_tile.html'), name='style_tile'),
]
