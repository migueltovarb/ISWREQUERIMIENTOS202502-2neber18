from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = [
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
        ('administrador', 'Administrador'),
    ]

    rol = models.CharField(max_length=20, choices=ROLES, default='estudiante')

    def __str__(self):
        return f"{self.username} ({self.rol})"


class Sala(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'En mantenimiento'),
    ]

    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    horarios_restringidos = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.estado}"


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    sala = models.ForeignKey('Sala', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario} en {self.sala} el {self.fecha}"
