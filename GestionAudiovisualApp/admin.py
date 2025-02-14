from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(TipoEquipo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(TecnologiaConexion)
# admin.site.register(Equipo)
# admin.site.register(Usuario)
# admin.site.register(Empleado)
# admin.site.register(Prestamo)




