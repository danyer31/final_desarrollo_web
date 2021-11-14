from django.contrib import admin
from .models import Almacen, Sucursal, Venta, Cliente, Modelo, Producto

admin.site.register(Almacen)
admin.site.register(Sucursal)
admin.site.register(Cliente)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Venta)
# Register your models here.
