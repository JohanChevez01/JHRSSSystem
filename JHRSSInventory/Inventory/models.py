# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.
# CATALOGOS
@python_2_unicode_compatible
class Departamento(models.Model):
	departamento=models.CharField(max_length=50)
	
	def __str__(self):
		return self.departamento

@python_2_unicode_compatible
class Cargo(models.Model):
	cargo=models.CharField(max_length=50)
	departamento=models.ForeignKey(Departamento)

	def __str__(self):
		return self.cargo

@python_2_unicode_compatible
class Genero(models.Model):
	genero=models.CharField(max_length=25)

	def __str__(self):
		return self.genero	

@python_2_unicode_compatible
class GradoAcademico(models.Model):
	gradoacademico=models.CharField(max_length=50)

	def __str__(self):
		return self.gradoacademico
		
@python_2_unicode_compatible
class EstadoCivil(models.Model):
	estadocivil=models.CharField(max_length=25)

	def __str__(self):
		return self.estadocivil

@python_2_unicode_compatible
class Regional(models.Model):
	regional=models.CharField(max_length=50)

	def __str__(self):
		return self.regional

@python_2_unicode_compatible
class ComentarioEmpleadoD(models.Model):
	comentarioEmpleadoD=models.CharField(max_length=250)

	def __str__(self):
		return self.comentarioEmpleadoD	

@python_2_unicode_compatible
class ComentarioEmpleadoT(models.Model):
	comentarioEmpleadoT=models.CharField(max_length=250)

	def __str__(self):
		return self.comentarioEmpleadoT	

@python_2_unicode_compatible
class ComentarioSalario(models.Model):
	comentarioSalario=models.CharField(max_length=25)

	def __str__(self):
		return self.comentarioSalario	

@python_2_unicode_compatible
class EstadoEquipo(models.Model):
	estado_equipo=models.CharField(max_length=50)

	def __str__(self):
		return self.estado_equipo

@python_2_unicode_compatible
class SistemaOperativo(models.Model):
	sistema=models.CharField(max_length=50)

	def __str__(self):
		return self.sistema

@python_2_unicode_compatible
class DiscoDuro(models.Model):
	disco=models.CharField(max_length=25)

	def __str__(self):
		return self.disco

@python_2_unicode_compatible
class Procesador(models.Model):
	procesador=models.CharField(max_length=25)

	def __str__(self):
		return self.procesador

@python_2_unicode_compatible
class RAM(models.Model):
	ram=models.CharField(max_length=25)

	def __str__(self):
		return self.ram

@python_2_unicode_compatible
class TipoEquipo(models.Model):
	tipo=models.CharField(max_length=50)

	def __str__(self):
		return self.tipo

@python_2_unicode_compatible
class Marca(models.Model):
	tipo = models.ForeignKey(TipoEquipo,on_delete=models.CASCADE)
	marca = models.CharField(max_length=50)

	def __str__(self):
		return self.marca

@python_2_unicode_compatible
class Modelo(models.Model):
	modelo = models.CharField(max_length=100)
	marca  = models.ForeignKey(Marca,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.modelo
# Transaccionales

@python_2_unicode_compatible
class Empleado(models.Model):
	cod_empleado=models.CharField(max_length=6)
	identidad=models.CharField(max_length=15)
	primer_nombre=models.CharField(max_length=50)
	segundo_nombre=models.CharField(max_length=50,null=True,blank=True)
	primer_apellido=models.CharField(max_length=50)
	segundo_apellido=models.CharField(max_length=50,null=True,blank=True)
	correo=models.EmailField()
	fechanacimiento=models.DateField()
	genero=models.ForeignKey(Genero) #on_delete=models.PROTECT
	estadocivil=models.ForeignKey(EstadoCivil)
	cargo=models.ForeignKey(Cargo)
	regional=models.ForeignKey(Regional)
	user= models.OneToOneField(User,null=True,blank=True)
	estado=models.BooleanField()

	def __str__(self):
		return self.primer_nombre +' '+ self.primer_apellido

@python_2_unicode_compatible
class DireccionEmpleado(models.Model):
	Empleado=models.ForeignKey(Empleado)
	direccion=models.CharField(max_length=300)
	Comentario=models.ForeignKey(ComentarioEmpleadoD)

	def __str__(self):
		return self.direccion

@python_2_unicode_compatible
class TelefonoEmpleado(models.Model):
	cod_empleado=models.ForeignKey(Empleado)
	telefono=models.CharField(max_length=15)
	Comentario=models.ForeignKey(ComentarioEmpleadoT)

	def __str__(self):
		return self.telefono

@python_2_unicode_compatible
class Contrato(models.Model):
	cod_empleado=models.ForeignKey(Empleado)
	fecha_inicio=models.DateField()
	fecha_final=models.DateField()

	def __str__(self):
		return self.cod_empleado.primer_nombre +' '+ self.cod_empleado.primer_apellido

@python_2_unicode_compatible
class Salario(models.Model):
	contrato=models.ForeignKey(Contrato)
	salario=models.DecimalField(blank=True,null=True, decimal_places=2, max_digits=10)
	fechaS=models.DateField()
	comentarioSalario=models.ForeignKey(ComentarioSalario,null=True,blank=True)

	def __str__(self):
		return self.salario

@python_2_unicode_compatible
class Profesion(models.Model):
	cod_empleado=models.ForeignKey(Empleado)
	profesion=models.CharField(max_length=50)
	gradoacademico=models.ForeignKey(GradoAcademico)

	def __str__(self):
		return self.profesion

@python_2_unicode_compatible
class EmpresaProveedor(models.Model):
	RTN=models.CharField(max_length=20)
	nombre=models.CharField(max_length=200)
	correo=models.EmailField(null=True,blank=True)

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class DireccionProveedor(models.Model):
	EmpresaProveedor=models.ForeignKey(EmpresaProveedor)
	direccion=models.CharField(max_length=300)
	Comentario=models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return self.direccion

@python_2_unicode_compatible
class TelefonoProveedor(models.Model):
	EmpresaProveedor=models.ForeignKey(EmpresaProveedor)
	telefono=models.CharField(max_length=15)
	Comentario=models.CharField(max_length=200,null=True,blank=True)

	def __str__(self):
		return self.telefono

@python_2_unicode_compatible
class InventarioEquipo(models.Model):
	codigo_Inventario=models.CharField(max_length=11)
	codigo_equipo=models.CharField(max_length=12)
	sistema=models.ForeignKey(SistemaOperativo)
	disco=models.ForeignKey(DiscoDuro)
	ram=models.ForeignKey(RAM)
	procesador=models.ForeignKey(Procesador)
	modelo=models.ForeignKey(Modelo)
	fecha_ingreso=models.DateField(auto_now_add=True)
	serial=models.CharField(max_length=50)
	n_orden_compra=models.CharField(max_length=20,null=True,blank=True)
	descripcion=models.CharField(max_length=50)
	empresaProveedor=models.ForeignKey(EmpresaProveedor)
	regional=models.ForeignKey(Regional)
	estado_equipo=models.ForeignKey(EstadoEquipo)
	estado=models.BooleanField(default=False)

	def __str__(self):
		return self.codigo_equipo

@python_2_unicode_compatible
class OtroInventario(models.Model):
	codigo_Inventario=models.CharField(max_length=11)
	modelo=models.ForeignKey(Modelo)
	serial=models.CharField(max_length=50)
	n_orden_compra=models.CharField(max_length=20,null=True,blank=True)
	descripcion=models.CharField(max_length=50)
	empresaProveedor=models.ForeignKey(EmpresaProveedor)
	regional=models.ForeignKey(Regional)
	fecha_ingreso=models.DateField(auto_now_add=True)
	estado_equipo=models.ForeignKey(EstadoEquipo)
	estado=models.BooleanField(default=False)

	def __str__(self):
		return self.codigo_Inventario

@python_2_unicode_compatible
class Mantenimiento(models.Model):
	codigo_equipo=models.ForeignKey(InventarioEquipo)
	fecha_inicio=models.DateField(auto_now_add=True)
	causa_Falla=models.TextField()
	accion_Realizar=models.TextField()
	fecha_salida=models.DateField(null=True,blank=True)
	cod_empleado=models.ForeignKey(Empleado)

	def __str__(self):
		return self.codigo_equipo

@python_2_unicode_compatible
class OtroMantenimiento(models.Model):
	codigo_Inventario=models.ForeignKey(OtroInventario)
	fecha_inicio=models.DateField(auto_now_add=True)
	causa_Falla=models.TextField()
	accion_Realizar=models.TextField()
	fecha_salida=models.DateField(null=True,blank=True)
	proveedor=models.ForeignKey(EmpresaProveedor)
	cod_empleado=models.ForeignKey(Empleado)

	def __str__(self):
		return self.codigo_Inventario

@python_2_unicode_compatible
class Asignacion(models.Model):
	codigo_equipo=models.ForeignKey(InventarioEquipo)
	cod_empleadoRecibe=models.ForeignKey(Empleado, related_name="Recibe")
	cod_empleadoEntrega=models.ForeignKey(Empleado, related_name="Entrega")
	fecha=models.DateField(auto_now_add=True)
	Comentario=models.CharField(max_length=200,null=True,blank=True)
	estadoAsignacion=models.BooleanField(default=True)
	
	def __str__(self):
		return "{}".format(self.codigo_equipo)

@python_2_unicode_compatible
class AsignacionImpresoras(models.Model):
	codigo_Inventario=models.ForeignKey(OtroInventario)
	cod_empleadoRecibe=models.ForeignKey(Empleado, related_name="ERecibe")
	cod_empleadoEntrega=models.ForeignKey(Empleado, related_name="EEntrega")
	fecha=models.DateField(auto_now_add=True)
	Comentario=models.CharField(max_length=200,null=True,blank=True)
	estadoAsignacion=models.BooleanField(default=True)
	
	def __str__(self):
		return "{}".format(self.codigo_Inventario)

@python_2_unicode_compatible
class Garantia(models.Model):
	N_Caso=models.CharField(max_length=20)
	codigo_equipo=models.ForeignKey(InventarioEquipo)
	Asunto=models.CharField(max_length=250)
	Fecha_aperturaCaso=models.DateField()
	Fecha_entregaProducto=models.DateField(null=True,blank=True)
	cod_empleado=models.ForeignKey(Empleado)

	def __str__(self):
		return self.Asunto



