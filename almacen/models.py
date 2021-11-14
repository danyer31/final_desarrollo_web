from django.db import models
from django.db.models.base import Model

# Create your models here.

class Almacen(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nombre

class Sucursal(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=256)
    telefono = models.IntegerField()

    def __str__(self) -> str:
        return self.direccion

class Cliente(models.Model):
    nit = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256)
    color = models.CharField(max_length=256)
    talla = models.IntegerField()
    precio = models.FloatField()

    def __str__(self) -> str:
        return self.nombre

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.fecha