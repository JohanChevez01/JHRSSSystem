from django.contrib import admin
from django.db import connections
from .models import *
# Register your models here.

admin.site.register(Departamento)
admin.site.register(Cargo)
admin.site.register(Genero)
admin.site.register(EstadoCivil)
admin.site.register(GradoAcademico)
admin.site.register(Regional)
admin.site.register(ComentarioEmpleadoD)
admin.site.register(ComentarioEmpleadoT)
admin.site.register(ComentarioSalario)
admin.site.register(EstadoEquipo)
admin.site.register(SistemaOperativo)
admin.site.register(RAM)
admin.site.register(Procesador)
admin.site.register(DiscoDuro)
admin.site.register(TipoEquipo)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Empleado)
admin.site.register(DireccionEmpleado)
admin.site.register(TelefonoEmpleado)
admin.site.register(Contrato)
admin.site.register(Salario)
admin.site.register(EmpresaProveedor)
admin.site.register(Profesion)
admin.site.register(DireccionProveedor)
admin.site.register(TelefonoProveedor)
admin.site.register(InventarioEquipo)
admin.site.register(OtroInventario)
admin.site.register(Mantenimiento)
admin.site.register(OtroMantenimiento)
admin.site.register(Asignacion)
admin.site.register(AsignacionImpresoras)
admin.site.register(Garantia)



