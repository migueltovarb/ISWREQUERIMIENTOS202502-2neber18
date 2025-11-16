from django.db import models

# Create your models here.
from django.db import models

class vehiculo(models.Model):
    COLORLIST = (
        ('1', 'ROJO'),
        ('2', 'AZUL'),
        ('3', 'VERDE'),
    )

    placa = models.CharField(max_length=6)
    marca = models.CharField(max_length=10)
    color_vehiculo = models.CharField(max_length=1, choices=COLORLIST)
    modelo = models.IntegerField()

    def __str__(self):
        return self.placa
