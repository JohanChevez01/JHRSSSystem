from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import ListView
from django_xhtml2pdf.views import PdfMixin
from django.urls import reverse
from django.core import serializers


@login_required()
def admin(request):
	empleado=Empleado.objects.all().count()
	equipo=InventarioEquipo.objects.all().count()
	mantenimiento=Mantenimiento.objects.all().count()
	return render(request,'admin.html',{'empleado': empleado,'equipo': equipo, 'mantenimiento':mantenimiento})

@login_required()
def recursosH(request):
	empleado=Empleado.objects.all().count()
	return render(request,'recursoH.html',{'empleado': empleado})

@login_required()
def compras(request):
	return render(request,'compras.html')

@login_required()
def IT(request):
	return render(request,'IT.html')

#======================================================================================
#*********************        ADMINISTRADOR   DE  SOFTWARE     ************************
#======================================================================================

#======================================================================================
#===========================      USUARIO     =========================================
#======================================================================================

@login_required()
def usuario(request):
	user = User.objects.all()
	form = UsuarioForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'usuario.html',{'user':user,'form':form})

@login_required()
def editarusuario(request,id):
	editarusuario= User.objects.get(pk=id)
	
	if request.method=='GET':
		form=UsuarioForm(instance=editarusuario)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=UsuarioForm(request.POST,instance=editarusuario)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:usuario'))
	return render(request,'editarusuario.html',{'form':form})

@login_required()
def nuevousuario(request):
	if request.method == 'POST' :
		form = UsuarioForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('Inventory:usuario'))
		else:
			user=User.objects.all()
			return render(request,'empleado.html',{'user':user})
	else:
		return HttpResponse("Utilice el metodo POST")

#======================================================================================		
#=========================          EMPLEADO          =================================
#======================================================================================

@login_required()
def empleado(request):
	empleados= Empleado.objects.all()
	generos= Genero.objects.all()
	estadocivil=EstadoCivil.objects.all()
	cargos=Cargo.objects.all()
	regionales=Regional.objects.all()
	users=User.objects.all()
	telefonos=TelefonoEmpleado.objects.all()
	listaTelefono=[]
	for empleado in empleados:
		for telefono in telefonos:
			if telefono.cod_empleado==empleado.id:
				listaTelefono.append(telefono)
	return render(request,'empleado.html',{'empleado':empleados,'generos':generos,'estadocivil':estadocivil,'cargos':cargos,'regionales':regionales,'users':users,'telefonos':listaTelefono})

@login_required()
def editarempleado(request,id):
	editarempleado= Empleado.objects.get(pk=id)
	
	if request.method=='GET':
		form=EmpleadoForm(instance=editarempleado)
	else:
		form=EmpleadoForm(request.POST,instance=editarempleado)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:empleado'))
	return render(request,'editarempleado.html',{'form':form, 'empleado':editarempleado})

@login_required()
def equipoempleado(request,id):
	equipo=Asignacion.objects.filter(cod_empleadoRecibe= id, estadoAsignacion='True').values('codigo_equipo')
	lista=equipo.latest('codigo_equipo') 

	return JsonResponse(lista,safe=False)

@login_required()
def InformacionEquipo(request,id):	
	Equipo=InventarioEquipo.objects.filter(pk= id).values('codigo_equipo')
	lista=Equipo.latest('codigo_equipo') 

	return JsonResponse(lista,safe=False)

@login_required()
def EquipoEmpleadoEntrega(request,id):	
	equipo2=Asignacion.objects.filter(cod_empleadoEntrega= id,  estadoAsignacion='False').values('codigo_equipo')
	lista=equipo2.latest('codigo_equipo') 

	return JsonResponse(lista,safe=False)

@login_required()
def nuevoempleado(request):
	if request.method == 'POST' :
		empleado=Empleado()
		empleado.cod_empleado=request.POST['cod_empleado']
		empleado.identidad=request.POST['identidad']
		empleado.primer_nombre=request.POST['primerNombre']
		empleado.segundo_nombre=request.POST['segundoNombre']
		empleado.primer_apellido=request.POST['primerApellido']
		empleado.segundo_apellido=request.POST['segundoApellido']
		empleado.fechanacimiento=request.POST['fechaNacimiento']
		empleado.genero=Genero(request.POST['genero'])
		empleado.estadocivil=EstadoCivil(request.POST['estadoCivil'])
		empleado.cargo=Cargo(request.POST['cargo'])
		empleado.regional=Regional(request.POST['regional'])
		empleado.user=User(request.POST['user'])
		empleado.correo=request.POST['email']

		if request.POST['estado'] == 'on':
			empleado.estado=True
		else:
			empleado.estado=False
		empleado.save()

		return HttpResponseRedirect(reverse('Inventory:empleado'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============TELEFONO EMPLEADO==================================
#================================================================
@login_required()
def telefonoempleado(request):
	telefonoempleado= TelefonoEmpleado.objects.all()
	empleado=Empleado.objects.all()
	comentario=ComentarioEmpleadoT.objects.all()
	return render(request,'telefonoempleado.html',{'telefonoempleado':telefonoempleado,'empleado':empleado,'comentario':comentario})

@login_required()
def editartelefonoempleado(request,id):
	editartelefonoempleado= TelefonoEmpleado.objects.get(pk=id)
	

	if request.method=='GET':
		form=TelefonoEmpleadoForm(instance=editartelefonoempleado)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=TelefonoEmpleadoForm(request.POST,instance=editartelefonoempleado)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoempleado'))
	return render(request,'editartelefonoempleado.html',{'form':form})

@login_required()
def nuevotelefonoempleado(request):
	if request.method == 'POST' :
		telefonoE=TelefonoEmpleado()
		telefonoE.cod_empleado=Empleado(request.POST['empleado'])
		telefonoE.telefono=request.POST['telefono']
		telefonoE.Comentario=ComentarioEmpleadoT(request.POST['comentario'])

		telefonoE.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoempleado'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminartelefonoempleado(request,id):
	telefono=TelefonoEmpleado.objects.get(id=id);
	telefono.delete()
	return HttpResponseRedirect(reverse('Inventory:telefonoempleado'))

#================================================================
#=============DIRECCION EMPLEADO=================================
#================================================================
@login_required()
def direccionempleado(request):
	direccionempleado= DireccionEmpleado.objects.all()
	empleado=Empleado.objects.all()
	comentario=ComentarioEmpleadoD.objects.all()
	return render(request,'direccionempleado.html',{'direccionempleado':direccionempleado,'empleado':empleado,'comentario':comentario})

@login_required()
def editardireccionempleado(request,id):
	editardireccionempleado= DireccionEmpleado.objects.get(pk=id)
	

	if request.method=='GET':
		form=DireccionEmpleadoForm(instance=editardireccionempleado)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DireccionEmpleadoForm(request.POST,instance=editardireccionempleado)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:direccionempleado'))
	return render(request,'editardireccionempleado.html',{'form':form})

@login_required()
def nuevodireccionempleado(request):
	if request.method == 'POST' :
		direccionE=DireccionEmpleado()
		direccionE.Empleado=Empleado(request.POST['empleado'])
		direccionE.direccion=request.POST['direccion']
		direccionE.Comentario=ComentarioEmpleadoD(request.POST['comentario'])

		direccionE.save()
		return HttpResponseRedirect(reverse('Inventory:direccionempleado'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminardireccionempleado(request,id):
	direccion=DireccionEmpleado.objects.get(id=id);
	direccion.delete()
	return HttpResponseRedirect(reverse('Inventory:direccionempleado'))

#================================================================
#=============CONTRATO===========================================
#================================================================
@login_required()
def contrato(request):
	contrato= Contrato.objects.all()
	empleados=Empleado.objects.all()
	return render(request,'contrato.html',{'contrato':contrato,'empleados':empleados})

@login_required()
def editarcontrato(request,id):
	editarcontrato= Contrato.objects.get(pk=id)

	if request.method=='GET':
		form=ContratoForm(instance=editarcontrato)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ContratoForm(request.POST,instance=editarcontrato)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:contrato'))
	return render(request,'editarcontrato.html',{'form':form})

@login_required()
def nuevocontrato(request):
	if request.method == 'POST' :
		contrato=Contrato()
		contrato.cod_empleado=Empleado(request.POST['CodEmpleado'])
		contrato.fecha_inicio=request.POST['fechaInicio']
		contrato.fecha_final=request.POST['fechaFinal']
		contrato.save()
		return HttpResponseRedirect(reverse('Inventory:contrato'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==============SALARIO===========================================
#================================================================
login_required()
def salario(request):
	salario= Salario.objects.all()
	contratos=Contrato.objects.all()
	comentarioS=ComentarioSalario.objects.all()
	return render(request,'salario.html',{'salario':salario,'contratos':contratos,'comentarioS':comentarioS})

@login_required()
def editarsalario(request,id):
	editarsalario= Salario.objects.get(pk=id)
	
	if request.method=='GET':
		form=SalarioForm(instance=editarsalario)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=SalarioForm(request.POST,instance=editarsalario)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:salario'))
	return render(request,'editarsalario.html',{'form':form})

@login_required()
def nuevosalario(request):
	if request.method == 'POST' :
		salario=Salario()
		salario.contrato=Contrato(request.POST['contrato'])
		salario.salario=request.POST['salario']
		salario.fechaS=request.POST['fechaSalario']
		salario.comentarioSalario=ComentarioSalario(request.POST['comentario'])
		salario.save()

		return HttpResponseRedirect(reverse('Inventory:salario'))
	else:
		return HttpResponse("Utilice el metodo POST")

#===============================================================================
#=============                 PROFESION                ========================
#===============================================================================
@login_required()
def profesion(request):
	profesion= Profesion.objects.all()
	empleado=Empleado.objects.all()
	gradoAcademico=GradoAcademico.objects.all()
	return render(request,'profesion.html',{'profesion':profesion,'gradoAcademico':gradoAcademico,'empleado':empleado})

@login_required()
def editarprofesion(request,id):
	editarprofesion= Profesion.objects.get(pk=id)

	if request.method=='GET':
		form=ProfesionForm(instance=editarprofesion)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProfesionForm(request.POST,instance=editarprofesion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:profesion'))
	return render(request,'editarprofesion.html',{'form':form})

@login_required()
def nuevoprofesion(request):
	if request.method == 'POST' :
		profesion=Profesion()
		profesion.cod_empleado=Empleado(request.POST['empleado'])
		profesion.profesion=request.POST['profesion']
		profesion.gradoacademico=GradoAcademico(request.POST['gradoAcademico'])
		profesion.save()

		return	HttpResponseRedirect(reverse('Inventory:profesion'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============CARGO==============================================
#================================================================
@login_required()
def cargo(request):
	cargo= Cargo.objects.all()
	depto=Departamento.objects.all()
	return render(request,'cargo.html',{'cargo':cargo,'deptos':depto})

@login_required()
def editarcargo(request,id):
	editarcargo= Cargo.objects.get(pk=id)
	if request.method=='GET':
		form=CargoForm(instance=editarcargo)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=CargoForm(request.POST,instance=editarcargo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:cargo'))
	return render(request,'editarcargo.html',{'form':form})

@login_required()
def nuevocargo(request):
	if request.method == 'POST' :
		cargo=Cargo()
		cargo.cargo=request.POST['cargo']
		cargo.departamento=Departamento(request.POST['deptos'])
		cargo.save()
		return HttpResponseRedirect(reverse('Inventory:cargo'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============DEPARTAMENTO=======================================
#================================================================
@login_required()
def departamento(request):
	departamento= Departamento.objects.all()
	return render(request,'departamento.html',{'departamento':departamento})

@login_required()
def editardepartamento(request,id):
	editardepartamento= Departamento.objects.get(pk=id)

	if request.method=='GET':
		form=DepartamentoForm(instance=editardepartamento)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DepartamentoForm(request.POST,instance=editardepartamento)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:departamento'))
	return render(request,'editardepartamento.html',{'form':form})

@login_required()
def nuevodepartamento(request):
	if request.method == 'POST' :
		departamento=Departamento()
		departamento.departamento=request.POST['departamento']

		departamento.save()
		return HttpResponseRedirect(reverse('Inventory:departamento'))
	else:
		return HttpResponse("Utilice el metodo POST")
#================================================================
#=================REGIONAL=======================================
#================================================================
@login_required()
def regional(request):
	regional= Regional.objects.all()
	return render(request,'regional.html',{'regional':regional})

@login_required()
def editarregional(request,id):
	editarregional= Regional.objects.get(pk=id)

	if request.method=='GET':
		form=RegionalForm(instance=editarregional)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=RegionalForm(request.POST,instance=editarregional)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:regional'))
	return render(request,'editarregional.html',{'form':form})

@login_required()
def nuevoregional(request):
	if request.method == 'POST' :
		regional=Regional()
		regional.regional=request.POST['regional']

		regional.save()
		return HttpResponseRedirect(reverse('Inventory:regional'))
	else:
		return HttpResponse("Utilice el metodo POST")

#======================================================================================		
#=====================================INVENTARIO EQUIPO================================
#======================================================================================

@login_required()
def equipo(request):
	equipo=InventarioEquipo.objects.all()
	modelo=Modelo.objects.all()
	marca=Marca.objects.all()
	tipo=TipoEquipo.objects.filter(tipo="Laptop") | TipoEquipo.objects.filter(tipo="Desktop")
	sistema=SistemaOperativo.objects.all()
	disco=DiscoDuro.objects.all()
	ram=RAM.objects.all()
	procesador=Procesador.objects.all()
	regionales=Regional.objects.all()
	proveedores=EmpresaProveedor.objects.all()
	estados=EstadoEquipo.objects.all()

	data={
		'equipo':equipo,
		'modelo':modelo,
		'marca':marca,
		'tipo':tipo,
		'sistema':sistema,
		'disco':disco,
		'ram':ram,
		'procesador':procesador,
		'regionales':regionales,
		'proveedores':proveedores,
		'estados':estados,
	}
	return render(request,'equipo.html',data)

@login_required()
def editarequipo(request,id):
	editarequipo= InventarioEquipo.objects.get(pk=id)
	
	if request.method=='GET':
		form=EquipoForm(instance=editarequipo)
	else:
		form=EquipoForm(request.POST,instance=editarequipo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:equipo'))
	return render(request,'editarequipo.html',{'form':form})

@login_required()
def nuevoequipo(request):
	if request.method == 'POST' :
		equipo=InventarioEquipo()
		equipo.codigo_Inventario=request.POST['codInventario']
		equipo.codigo_equipo=request.POST['codEquipo']
		equipo.tipo=TipoEquipo(request.POST['tipo'])
		equipo.sistema=SistemaOperativo(request.POST['sistema'])
		equipo.disco=DiscoDuro(request.POST['disco'])
		equipo.ram=RAM(request.POST['ram'])
		equipo.procesador=Procesador(request.POST['procesador'])
		equipo.marca=Marca(request.POST['marca'])
		equipo.modelo=Modelo(request.POST['modelo'])
		equipo.descripcion=request.POST['descripcion']
		equipo.serial=request.POST['serial']
		equipo.n_orden_compra=request.POST['ordencompra']
		equipo.empresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		equipo.regional=Regional(request.POST['regional'])
		equipo.estado_equipo=EstadoEquipo(request.POST['estado'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:equipo'))
	else:
		return HttpResponse("Utilice el metodo POST")

def marca_json(request):
	if request.is_ajax():
		valor=request.GET['id']
		if valor:
			marcas = Marca.objects.filter(tipo = TipoEquipo.objects.get(pk= valor))

			html = ''
			if marcas:
				html += '''
					<option selected="">Seleccione Marca</option>'''
				for x in marcas:
					html += '''
						<option value="{}">{}</option>'''.format(x.id,x.marca)
			else:
				html += '''
					<option selected="">No hay marcas diponibles</option>
				'''
			return JsonResponse({'contenido': html})
	else:
		pass

def modelo_json(request):
	if request.is_ajax():
		valor1=request.GET['id2']
		if valor1:
			modelos = Modelo.objects.filter(marca = Marca.objects.get(pk= valor1))

			html = ''
			if modelos:
				html += '''
					<option selected="">Seleccione Modelo</option>'''
				for y in modelos:
					html += '''
						<option value="{}">{}</option>'''.format(y.id,y.modelo)
			else:
				html += '''
					<option selected="">No hay modelos diponibles</option>
				'''
			return JsonResponse({'contenModelo': html})
	else:
		pass

#======================================================================================		
#===========================  INVENTARIO IMPRESORAS  & MAS   ==========================
#======================================================================================

@login_required()
def impresoras(request):
	equipo=OtroInventario.objects.all()
	modelo=Modelo.objects.all()
	marca=Marca.objects.all()
	tipo=TipoEquipo.objects.filter(tipo="Impresora") | TipoEquipo.objects.filter(tipo="Pantallas") | TipoEquipo.objects.filter(tipo="UPS") | TipoEquipo.objects.filter(tipo="Docking Station") | TipoEquipo.objects.filter(tipo="Router") | TipoEquipo.objects.filter(tipo="Telefono IP")
	regionales=Regional.objects.all()
	proveedores=EmpresaProveedor.objects.all()
	estados=EstadoEquipo.objects.all()

	data={
		'equipo':equipo,
		'regionales':regionales,
		'proveedores':proveedores,
		'estados':estados,
		'modelo':modelo,
		'marca':marca,
		'tipo':tipo,
	}
	return render(request,'impresoras.html',data)

@login_required()
def editarimpresoras(request,id):
	editarimpresoras= OtroInventario.objects.get(pk=id)
	
	if request.method=='GET':
		form=ImpresorasForm(instance=editarimpresoras)
	else:
		form=ImpresorasForm(request.POST,instance=editarimpresoras)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:impresoras'))
	return render(request,'editarimpresoras.html',{'form':form})

@login_required()
def nuevoimpresoras(request):
	if request.method == 'POST' :
		equipo=OtroInventario()
		equipo.codigo_Inventario=request.POST['codInventario']
		equipo.tipo=TipoEquipo(request.POST['tipo'])
		equipo.marca=Marca(request.POST['marca'])
		equipo.modelo=Modelo(request.POST['modelo'])
		equipo.serial=request.POST['serial']
		equipo.n_orden_compra=request.POST['ordencompra']
		equipo.descripcion=request.POST['descripcion']
		equipo.empresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		equipo.regional=Regional(request.POST['regional'])
		equipo.estado_equipo=EstadoEquipo(request.POST['estado'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:impresoras'))
	else:
		return HttpResponse("Utilice el metodo POST")

def marcai_json(request):
	if request.is_ajax():
		valor=request.GET['id']
		if valor:
			marcas = Marca.objects.filter(tipo = TipoEquipo.objects.get(pk= valor))

			html = ''
			if marcas:
				html += '''
					<option selected="">Seleccione Marca</option>'''
				for x in marcas:
					html += '''
						<option value="{}">{}</option>'''.format(x.id,x.marca)
			else:
				html += '''
					<option selected="">No hay marcas diponibles</option>
				'''
			return JsonResponse({'contenido': html})
	else:
		pass
		
def modeloi_json(request):
	if request.is_ajax():
		valor1=request.GET['id2']
		if valor1:
			modelos = Modelo.objects.filter(marca = Marca.objects.get(pk= valor1))

			html = ''
			if modelos:
				html += '''
					<option selected="">Seleccione Modelo</option>'''
				for y in modelos:
					html += '''
						<option value="{}">{}</option>'''.format(y.id,y.modelo)
			else:
				html += '''
					<option selected="">No hay modelos diponibles</option>
				'''
			return JsonResponse({'contenModelo': html})
	else:
		pass

#================================================================
#=============ASIGNACION=========================================
#================================================================
@login_required()
def asignacion(request):
	asignacion=Asignacion.objects.all()
	estado=EstadoEquipo.objects.filter(estado_equipo="Disponible")
	equipos = InventarioEquipo.objects.filter(estado="False" , estado_equipo=estado)
	estadoAsignacion= Asignacion.objects.filter(estadoAsignacion="True")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'asignacion.html',{'estadoAsignacion':estadoAsignacion,'asignacion':asignacion,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editarasignacion(request,id):
	editarasignacion= Asignacion.objects.get(pk=id)
	
	if request.method=='GET':
		form=AsignacionForm(instance=editarasignacion)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=AsignacionForm(request.POST,instance=editarasignacion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:asignacion'))
	return render(request,'editarasignacion.html',{'form':form})

@login_required()
def nuevoasignacion(request):
	if request.method == 'GET' :
		asignacion=Asignacion()
		asignacion.codigo_equipo=InventarioEquipo(request.GET.get("selectCodEquipo"))
		asignacion.cod_empleadoRecibe=Empleado(request.GET.get("selectEmpleadoRecibe"))
		asignacion.cod_empleadoEntrega=Empleado(request.GET.get("selectEmpleadoEntrega"))
		asignacion.Comentario=request.GET.get('Comentario')
		asignacion.estadoAsignacion="True"
		asignacion.save()
		equipo=InventarioEquipo.objects.get(pk=request.GET.get("selectCodEquipo"))
		equipo.estado="True"
		equipo.save()

		ctx={
			'Hola':'Hola'
		}
		return JsonResponse(ctx,safe=False)
	else:
		return JsonResponse(ctx,safe=False)

#================================================================
#=============   ASIGNACION IMPRESORAS   ========================
#================================================================
@login_required()
def asignacionImpresoras(request):
	asignacion=AsignacionImpresoras.objects.all()
	estado=EstadoEquipo.objects.filter(estado_equipo="Disponible")
	equipos = OtroInventario.objects.filter(estado="False" , estado_equipo=estado)
	estadoAsignacion= AsignacionImpresoras.objects.filter(estadoAsignacion="True")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'asignacionImpresoras.html',{'estadoAsignacion':estadoAsignacion,'asignacion':asignacion,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editarasignacionImpresoras(request,id):
	editarasignacion= AsignacionImpresoras.objects.get(pk=id)
	
	if request.method=='GET':
		form=AsignacionForm(instance=editarasignacion)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=AsignacionForm(request.POST,instance=editarasignacion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:asignacionImpresoras'))
	return render(request,'editarasignacionImpresora.html',{'form':form})

@login_required()
def nuevoasignacionImpresoras(request):
	if request.method == 'GET' :
		asignacion=AsignacionImpresoras()
		asignacion.codigo_Inventario=OtroInventario(request.GET.get("selectCodEquipo"))
		asignacion.cod_empleadoRecibe=Empleado(request.GET.get("selectEmpleadoRecibe"))
		asignacion.cod_empleadoEntrega=Empleado(request.GET.get("selectEmpleadoEntrega"))
		asignacion.Comentario=request.GET.get('Comentario')
		asignacion.estadoAsignacion="True"
		asignacion.save()
		equipo=OtroInventario.objects.get(pk=request.GET.get("selectCodEquipo"))
		equipo.estado="True"
		equipo.save()

		ctx={
			'Hola':'Hola'
		}
		return JsonResponse(ctx,safe=False)
	else:
		return JsonResponse(ctx,safe=False)

#================================================================
#==================== DESCARGO  =================================
#================================================================

@login_required()
def descargo(request):
	descargo=Asignacion.objects.all()
	equipos = InventarioEquipo.objects.filter(estado="True")
	estadoAsignacion= Asignacion.objects.filter(estadoAsignacion="False")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)

	return render(request,'descargo.html',{'estadoAsignacion':estadoAsignacion,'descargo':descargo,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def nuevodescargo(request):
	if request.method == 'POST' :
		descargo=Asignacion()
		descargo.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		descargo.cod_empleadoRecibe=Empleado(request.POST['CodEmpleadoRecibe'])
		descargo.cod_empleadoEntrega=Empleado(request.POST['idEntrega'])
		descargo.Comentario=request.POST['Comentario']
		descargo.estadoAsignacion="False"
		descargo.save()

		equipo=InventarioEquipo.objects.get(pk=request.POST['CodEquipo'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:descargo'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def Entregadescargo(request,pk):	
	empleado=Asignacion.objects.filter(codigo_equipo= pk, estadoAsignacion='True').values('cod_empleadoRecibe')
	lista=empleado.latest('cod_empleadoRecibe') 

	return JsonResponse(lista,safe=False)

@login_required()
def EmpleadoEntrega(request,pk):	
	empleado=Empleado.objects.filter(pk= pk).values('primer_nombre','primer_apellido')
	lista=empleado.latest('primer_nombre') 

	return JsonResponse(lista,safe=False)


#================================================================
#==================== DESCARGO  IMPRESORAS   ====================
#================================================================

@login_required()
def descargoImpresoras(request):
	descargo=AsignacionImpresoras.objects.all()
	equipos = OtroInventario.objects.filter(estado="True")
	estadoAsignacion= AsignacionImpresoras.objects.filter(estadoAsignacion="False")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)

	return render(request,'descargoImpresoras.html',{'estadoAsignacion':estadoAsignacion,'descargo':descargo,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def nuevodescargoImpresoras(request):
	if request.method == 'POST' :
		descargo=AsignacionImpresoras()
		descargo.codigo_Inventario=OtroInventario(request.POST['CodEquipo'])
		descargo.cod_empleadoRecibe=Empleado(request.POST['CodEmpleadoRecibe'])
		descargo.cod_empleadoEntrega=Empleado(request.POST['idEntrega'])
		descargo.Comentario=request.POST['Comentario']
		descargo.estadoAsignacion="False"
		descargo.save()

		equipo=OtroInventario.objects.get(pk=request.POST['CodEquipo'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:descargoImpresoras'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def EntregadescargoImpresoras(request,pk):	
	empleado=AsignacionImpresoras.objects.filter(codigo_Inventario= pk, estadoAsignacion='True').values('cod_empleadoRecibe')
	lista=empleado.latest('cod_empleadoRecibe') 

	return JsonResponse(lista,safe=False)

@login_required()
def EmpleadoEntregaImpresoras(request,pk):	
	empleado=Empleado.objects.filter(pk= pk).values('primer_nombre','primer_apellido')
	lista=empleado.latest('primer_nombre') 

	return JsonResponse(lista,safe=False)

#================================================================
#=============MANTENIMIENTO======================================
#================================================================
@login_required()
def mantenimiento(request):
	mantenimiento= Mantenimiento.objects.all()
	equipos=InventarioEquipo.objects.all()
	empleados=Empleado.objects.all()
	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id== cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'mantenimiento.html',{'mantenimiento':mantenimiento,'empleados':empleados,'equipos':equipos,'departamento':departamento,'cargos':cargos,'listaEmpleados':listaEmpleados})

@login_required()
def editarmantenimiento(request,id):
	editarmantenimiento= Mantenimiento.objects.get(pk=id)

	if request.method=='GET':
		form=MantenimientoForm(instance=editarmantenimiento)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MantenimientoForm(request.POST,instance=editarmantenimiento)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimiento'))
	return render(request,'editarmantenimiento.html',{'form':form})

@login_required()
def nuevomantenimiento(request):
	if request.method == 'POST' :
		mantenimiento=Mantenimiento()
		mantenimiento.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		mantenimiento.causa_Falla=request.POST['causa']
		mantenimiento.accion_Realizar=request.POST['realizar']
		mantenimiento.fecha_salida=request.POST['fechaSalida']
		mantenimiento.cod_empleado=Empleado(request.POST['CodEmpleado'])
		mantenimiento.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimiento'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============MANTENIMIENTO de Impresoras =======================
#================================================================
@login_required()
def mantenimientoImpresora(request):
	mantenimiento= OtroMantenimiento.objects.all()
	equipos=OtroInventario.objects.all()
	proveedor=EmpresaProveedor.objects.all()
	empleados=Empleado.objects.all()
	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id== cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'mantenimientoImpresora.html',{'mantenimiento':mantenimiento,'proveedor':proveedor,'empleados':empleados,'equipos':equipos,'departamento':departamento,'cargos':cargos,'listaEmpleados':listaEmpleados})

@login_required()
def editarmantenimientoImpresora(request,id):
	editarmantenimientoImpresora= OtroMantenimiento.objects.get(pk=id)

	if request.method=='GET':
		form=MantenimientoImpresorasForm(instance=editarmantenimientoImpresora)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MantenimientoImpresorasForm(request.POST,instance=editarmantenimientoImpresora)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimientoImpresora'))
	return render(request,'editarotromantenimiento.html',{'form':form})

@login_required()
def nuevomantenimientoImpresora(request):
	if request.method == 'POST' :
		mantenimiento=OtroMantenimiento()
		mantenimiento.codigo_Inventario=OtroInventario(request.POST['CodInventario'])
		mantenimiento.causa_Falla=request.POST['causa']
		mantenimiento.accion_Realizar=request.POST['realizar']
		mantenimiento.fecha_salida=request.POST['fechaSalida']
		mantenimiento.proveedor=EmpresaProveedor(request.POST['Codproveedor'])
		mantenimiento.cod_empleado=Empleado(request.POST['CodEmpleado'])
		mantenimiento.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimientoImpresora'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============     GARANTIA     =================================
#================================================================
@login_required()
def garantia(request):
	garantia= Garantia.objects.all()
	equipo=InventarioEquipo.objects.all()
	empleados=Empleado.objects.all()
	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id== cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'garantia.html',{'garantia':garantia,'empleados':empleados,'equipo':equipo,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editargarantia(request,id):
	editargarantia= Garantia.objects.get(pk=id)
	
	if request.method=='GET':
		form=GarantiaForm(instance=editargarantia)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=GarantiaForm(request.POST,instance=editargarantia)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:garantia'))
	return render(request,'editargarantia.html',{'form':form})

@login_required()
def nuevogarantia(request):
	if request.method == 'POST' :
		garantia=Garantia()
		garantia.N_Caso=request.POST['caso']
		garantia.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		garantia.Asunto=request.POST['asunto']
		garantia.Fecha_aperturaCaso=request.POST['fechaApertura']
		garantia.Fecha_entregaProducto=request.POST['fechaEntrega']
		garantia.cod_empleado=Empleado(request.POST['CodEmpleado'])

		garantia.save()
		return HttpResponseRedirect(reverse('Inventory:garantia'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=================== Tipo EQUIPO ================================
#================================================================
@login_required()
def tipoEquipo(request):
	tipo= TipoEquipo.objects.all()
	return render(request,'tipoEquipo.html',{'tipo':tipo})

@login_required()
def editartipoEquipo(request,id):
	editartipoEquipo=TipoEquipo.objects.get(pk=id)

	if request.method=='GET':
		form=tipoEquipoForm(instance=editartipoEquipo)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=tipoEquipoForm(request.POST,instance=editartipoEquipo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:tipoEquipo'))
	return render(request,'editartipoEquipo.html',{'form':form})

@login_required()
def nuevotipoEquipo(request):
	if request.method == 'POST' :
		tipo=TipoEquipo()
		tipo.tipo=request.POST['tipo']

		tipo.save()
		return HttpResponseRedirect(reverse('Inventory:tipoEquipo'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#================== MARCA DE EQUIPO =============================
#================================================================
@login_required()
def marca(request):
	marca= Marca.objects.all()
	tipo=TipoEquipo.objects.all()
	return render(request,'marca.html',{'marca':marca,'tipo':tipo})

@login_required()
def editarmarca(request,id):
	editarmarca=Marca.objects.get(pk=id)

	if request.method=='GET':
		form=MarcaForm(instance=editarmarca)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MarcaForm(request.POST,instance=editarmarca)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:marca'))
	return render(request,'editarmarca.html',{'form':form})

@login_required()
def nuevomarca(request):
	if request.method == 'POST' :
		marca=Marca()
		marca.marca=request.POST['marca']
		marca.tipo=TipoEquipo(request.POST['tipo'])
		marca.save()
		return HttpResponseRedirect(reverse('Inventory:marca'))
	else:
		return HttpResponse("Utilice el metodo POST")

#=================================================================
#=============        MODELO              ========================
#=================================================================
@login_required()
def modelo(request):
	modelo= Modelo.objects.all()
	marca=Marca.objects.all()
	return render(request,'modelo.html',{'modelo':modelo,'marca':marca})

@login_required()
def editarmodelo(request,id):
	editarmodelo= Modelo.objects.get(pk=id)

	if request.method=='GET':
		form=ModeloForm(instance=editarmodelo)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ModeloForm(request.POST,instance=editarmodelo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:modelo'))
	return render(request,'editarmodelo.html',{'form':form})

@login_required()
def nuevomodelo(request):
	if request.method == 'POST' :
		modelo=Modelo()
		modelo.marca=Marca(request.POST['marca'])
		modelo.modelo=request.POST['modelo']
		modelo.save()

		return	HttpResponseRedirect(reverse('Inventory:modelo'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#============= SISTEMA OPERATIVO ================================
#================================================================
@login_required()
def sistema(request):
	sistema= SistemaOperativo.objects.all()
	return render(request,'sistema.html',{'sistema':sistema})

@login_required()
def editarsistema(request,id):
	editarsistema=SistemaOperativo.objects.get(pk=id)

	if request.method=='GET':
		form=SistemaForm(instance=editarsistema)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=SistemaForm(request.POST,instance=editarsistema)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:sistema'))
	return render(request,'editarsistema.html',{'form':form})

@login_required()
def nuevosistema(request):
	if request.method == 'POST' :
		sistema=SistemaOperativo()
		sistema.sistema=request.POST['sistema']

		sistema.save()
		return HttpResponseRedirect(reverse('Inventory:sistema'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==================== DISCO DURO ================================
#================================================================
@login_required()
def discoDuro(request):
	disco= DiscoDuro.objects.all()
	return render(request,'discoDuro.html',{'disco':disco})

@login_required()
def editardiscoDuro(request,id):
	editardiscoDuro=DiscoDuro.objects.get(pk=id)

	if request.method=='GET':
		form=discoDuroForm(instance=editardiscoDuro)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=discoDuroForm(request.POST,instance=editardiscoDuro)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:discoDuro'))
	return render(request,'editardiscoDuro.html',{'form':form})

@login_required()
def nuevodiscoDuro(request):
	if request.method == 'POST' :
		discoDuro=DiscoDuro()
		discoDuro.disco=request.POST['discoDuro']

		discoDuro.save()
		return HttpResponseRedirect(reverse('Inventory:discoDuro'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==================== MEMORIA RAM================================
#================================================================
@login_required()
def memoriaRAM(request):
	rams= RAM.objects.all()
	return render(request,'RAM.html',{'rams':rams})

@login_required()
def editarmemoriaRAM(request,id):
	editarRAM=RAM.objects.get(pk=id)

	if request.method=='GET':
		form=RAMForm(instance=editarRAM)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=RAMForm(request.POST,instance=editarRAM)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:memoriaRAM'))
	return render(request,'editarRAM.html',{'form':form})

@login_required()
def nuevomemoriaRAM(request):
	if request.method == 'POST' :
		ram=RAM()
		ram.ram=request.POST['memoriaRAM']

		ram.save()
		return HttpResponseRedirect(reverse('Inventory:memoriaRAM'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==================== PROCESADOR ================================
#================================================================
@login_required()
def procesador(request):
	procesador= Procesador.objects.all()
	return render(request,'procesador.html',{'procesador':procesador})

@login_required()
def editarprocesador(request,id):
	editarprocesador=Procesador.objects.get(pk=id)

	if request.method=='GET':
		form=ProcesadorForm(instance=editarprocesador)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProcesadorForm(request.POST,instance=editarprocesador)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:procesador'))
	return render(request,'editarprocesador.html',{'form':form})

@login_required()
def nuevoprocesador(request):
	if request.method == 'POST' :
		procesador=Procesador()
		procesador.procesador=request.POST['procesador']

		procesador.save()
		return HttpResponseRedirect(reverse('Inventory:procesador'))
	else:
		return HttpResponse("Utilice el metodo POST")

#==================================================================
#================PROVEEDOR=========================================
#==================================================================
@login_required()
def proveedor(request):
	proveedor= EmpresaProveedor.objects.all()
	return render(request,'proveedor.html',{'proveedor':proveedor})

@login_required()
def editarproveedor(request,id):
	editarproveedor= EmpresaProveedor.objects.get(pk=id)

	if request.method=='GET':
		form=ProveedorForm(instance=editarproveedor)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProveedorForm(request.POST,instance=editarproveedor)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:proveedor'))
	return render(request,'editarproveedor.html',{'form':form})

@login_required()
def nuevoproveedor(request):
	if request.method=='POST':
		proveedor=EmpresaProveedor()
		proveedor.RTN=request.POST['RTN']
		proveedor.nombre=request.POST['nombre']
		proveedor.correo=request.POST['correo']

		proveedor.save()
		return HttpResponseRedirect(reverse('Inventory:proveedor'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============DIRECCION PROVEEDOR=================================
#================================================================
@login_required()
def direccionproveedor(request):
	direccionproveedor= DireccionProveedor.objects.all()
	proveedor=EmpresaProveedor.objects.all()
	return render(request,'direccionproveedor.html',{'direccionproveedor':direccionproveedor,'proveedor':proveedor})

@login_required()
def editardireccionproveedor(request,id):
	editardireccionproveedor= DireccionProveedor.objects.get(pk=id)

	if request.method=='GET':
		form=DireccionProveedorForm(instance=editardireccionproveedor)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DireccionProveedorForm(request.POST,instance=editardireccionproveedor)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:direccionproveedor'))
	return render(request,'editardireccionproveedor.html',{'form':form})

@login_required()
def nuevodireccionproveedor(request):
	if request.method == 'POST' :
		direccion=DireccionProveedor()
		direccion.EmpresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		direccion.direccion=request.POST['direccion']
		direccion.Comentario=request.POST['comentario']

		direccion.save()
		return HttpResponseRedirect(reverse('Inventory:direccionproveedor'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminardireccionproveedor(request,id):
	direccion=DireccionProveedor.objects.get(id=id);
	direccion.delete()
	return HttpResponseRedirect(reverse('Inventory:direccionproveedor'))

#================================================================
#=============TELEFONO PROVEEDOR=================================
#================================================================
@login_required()
def telefonoproveedor(request):
	telefonoproveedor= TelefonoProveedor.objects.all()
	proveedor=EmpresaProveedor.objects.all()
	return render(request,'telefonoproveedor.html',{'telefonoproveedor':telefonoproveedor,'proveedor':proveedor})

@login_required()
def editartelefonoproveedor(request,id):
	editartelefonoproveedor= TelefonoProveedor.objects.get(pk=id)

	if request.method=='GET':
		form=TelefonoProveedorForm(instance=editartelefonoproveedor)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=TelefonoProveedorForm(request.POST,instance=editartelefonoproveedor)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoproveedor'))
	return render(request,'editartelefonoproveedor.html',{'form':form})

@login_required()
def nuevotelefonoproveedor(request):
	if request.method == 'POST' :
		telefono=TelefonoProveedor()
		telefono.EmpresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		telefono.telefono=request.POST['telefono']
		telefono.Comentario=request.POST['comentario']

		telefono.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoproveedor'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminartelefonoproveedor(request,id):
	telefono=TelefonoProveedor.objects.get(id=id);
	telefono.delete()
	return HttpResponseRedirect(reverse('Inventory:telefonoproveedor'))

#================================================================================
#***********************     RECURSOS      HUMANOS     **************************
#================================================================================

#================================================================================
#=============================== USUARIO RRHH ===================================
#================================================================================

@login_required()
def usuarioR(request):
	user = User.objects.all()
	form = UsuarioForm()
	for field in form.fields:
		form.fields[field].widget.attrs={
			'class': 'form-control',
			# 'style':'bdhsfdkjsnflk'
		}
	return render(request,'usuarioR.html',{'user':user,'form':form})

@login_required()
def editarusuarioR(request,id):
	editarusuarioR= User.objects.get(pk=id)
	
	if request.method=='GET':
		form=UsuarioForm(instance=editarusuarioR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=UsuarioForm(request.POST,instance=editarusuarioR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:usuarioR'))
	return render(request,'editarusuarioR.html',{'form':form})

@login_required()
def nuevousuarioR(request):
	if request.method == 'POST' :
		form = UsuarioForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('Inventory:usuarioR'))
		else:
			user=User.objects.all()
			return render(request,'empleadoR.html',{'user':user})
	else:
		return HttpResponse("Utilice el metodo POST")

#=========================================================================		
#=======================     EMPLEADO     RRHH     =======================
#=========================================================================

@login_required()
def empleadoR(request):
	empleados= Empleado.objects.all()
	generos= Genero.objects.all()
	estadocivil=EstadoCivil.objects.all()
	cargos=Cargo.objects.all()
	regionales=Regional.objects.all()
	users=User.objects.all()
	telefonos=TelefonoEmpleado.objects.all()
	listaTelefono=[]
	for empleado in empleados:
		for telefono in telefonos:
			if telefono.cod_empleado==empleado.id:
				listaTelefono.append(telefono)
	return render(request,'empleadoR.html',{'empleado':empleados,'generos':generos,'estadocivil':estadocivil,'cargos':cargos,'regionales':regionales,'users':users,'telefonos':listaTelefono})

@login_required()
def editarempleadoR(request,id):
	editarempleado= Empleado.objects.get(pk=id)
	
	if request.method=='GET':
		form=EmpleadoForm(instance=editarempleado)
	else:
		form=EmpleadoForm(request.POST,instance=editarempleado)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:empleadoR'))
	return render(request,'editarempleadoR.html',{'form':form, 'empleadoR':editarempleadoR})

@login_required()
def nuevoempleadoR(request):
	if request.method == 'POST' :
		empleado=Empleado()
		empleado.cod_empleado=request.POST['cod_empleado']
		empleado.identidad=request.POST['identidad']
		empleado.primer_nombre=request.POST['primerNombre']
		empleado.segundo_nombre=request.POST['segundoNombre']
		empleado.primer_apellido=request.POST['primerApellido']
		empleado.segundo_apellido=request.POST['segundoApellido']
		empleado.fechanacimiento=request.POST['fechaNacimiento']
		empleado.genero=Genero(request.POST['genero'])
		empleado.estadocivil=EstadoCivil(request.POST['estadoCivil'])
		empleado.cargo=Cargo(request.POST['cargo'])
		empleado.regional=Regional(request.POST['regional'])
		empleado.user=User(request.POST['user'])
		empleado.correo=request.POST['email']

		if request.POST['estado'] == 'on':
			empleado.estado=True
		else:
			empleado.estado=False
		empleado.save()

		return HttpResponseRedirect(reverse('Inventory:empleado'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#================     TELEFONO EMPLEADO RRHH     ================
#================================================================
@login_required()
def telefonoempleadoR(request):
	telefonoempleado= TelefonoEmpleado.objects.all()
	empleado=Empleado.objects.all()
	comentario=ComentarioEmpleadoT.objects.all()
	return render(request,'telefonoempleadoR.html',{'telefonoempleado':telefonoempleado,'empleado':empleado,'comentario':comentario})

@login_required()
def editartelefonoempleadoR(request,id):
	editartelefonoempleadoR= TelefonoEmpleado.objects.get(pk=id)
	
	if request.method=='GET':
		form=TelefonoEmpleadoForm(instance=editartelefonoempleadoR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=TelefonoEmpleadoForm(request.POST,instance=editartelefonoempleadoR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoempleadoR'))
	return render(request,'editartelefonoempleadoR.html',{'form':form})

@login_required()
def nuevotelefonoempleadoR(request):
	if request.method == 'POST' :
		telefonoE=TelefonoEmpleado()
		telefonoE.cod_empleado=Empleado(request.POST['empleado'])
		telefonoE.telefono=request.POST['telefono']
		telefonoE.Comentario=ComentarioEmpleadoT(request.POST['comentario'])

		telefonoE.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoempleadoR'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminartelefonoempleadoR(request,id):
	telefono=TelefonoEmpleado.objects.get(id=id);
	telefono.delete()
	return HttpResponseRedirect(reverse('Inventory:telefonoempleadoR'))
#================================================================
#================     DIRECCION EMPLEADO RRHH     ===============
#================================================================
@login_required()
def direccionempleadoR(request):
	direccionempleado= DireccionEmpleado.objects.all()
	empleado=Empleado.objects.all()
	comentario=ComentarioEmpleadoD.objects.all()
	return render(request,'direccionempleadoR.html',{'direccionempleado':direccionempleado,'empleado':empleado,'comentario':comentario})

@login_required()
def editardireccionempleadoR(request,id):
	editardireccionempleadoR= DireccionEmpleado.objects.get(pk=id)

	if request.method=='GET':
		form=DireccionEmpleadoForm(instance=editardireccionempleadoR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DireccionEmpleadoForm(request.POST,instance=editardireccionempleadoR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:direccionempleadoR'))
	return render(request,'editardireccionempleadoR.html',{'form':form})

@login_required()
def nuevodireccionempleadoR(request):
	if request.method == 'POST' :
		direccionE=DireccionEmpleado()
		direccionE.Empleado=Empleado(request.POST['empleado'])
		direccionE.direccion=request.POST['direccion']
		direccionE.Comentario=ComentarioEmpleadoD(request.POST['comentario'])

		direccionE.save()
		return HttpResponseRedirect(reverse('Inventory:direccionempleadoR'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminardireccionempleadoR(request,id):
	direccion=DireccionEmpleado.objects.get(id=id);
	direccion.delete()
	return HttpResponseRedirect(reverse('Inventory:direccionempleadoR'))
#================================================================
#==================     CONTRATO     RRHH     ===================
#================================================================
@login_required()
def contratoR(request):
	contrato= Contrato.objects.all()
	empleados=Empleado.objects.all()
	return render(request,'contratoR.html',{'contrato':contrato,'empleados':empleados})

@login_required()
def editarcontratoR(request,id):
	editarcontratoR= Contrato.objects.get(pk=id)
	
	if request.method=='GET':
		form=ContratoForm(instance=editarcontratoR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ContratoForm(request.POST,instance=editarcontratoR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:contratoR'))
	return render(request,'editarcontratoR.html',{'form':form})

@login_required()
def nuevocontratoR(request):
	if request.method == 'POST' :
		contrato=Contrato()
		contrato.cod_empleado=Empleado(request.POST['CodEmpleado'])
		contrato.fecha_inicio=request.POST['fechaInicio']
		contrato.fecha_final=request.POST['fechaFinal']
		contrato.save()
		return HttpResponseRedirect(reverse('Inventory:contratoR'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==============     SALARIO     RRHH     ========================
#================================================================
login_required()
def salarioR(request):
	salario= Salario.objects.all()
	contratos=Contrato.objects.all()
	comentarioS=ComentarioSalario.objects.all()
	return render(request,'salarioR.html',{'salario':salario,'contratos':contratos,'comentarioS':comentarioS})

@login_required()
def editarsalarioR(request,id):
	editarsalario= Salario.objects.get(pk=id)
	
	if request.method=='GET':
		form=SalarioForm(instance=editarsalario)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=SalarioForm(request.POST,instance=editarsalario)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:salarioR'))
	return render(request,'editarsalarioR.html',{'form':form})

@login_required()
def nuevosalarioR(request):
	if request.method == 'POST' :
		salario=Salario()
		salario.contrato=Contrato(request.POST['contrato'])
		salario.salario=request.POST['salario']
		salario.fechaS=request.POST['fechaSalario']
		salario.comentarioSalario=ComentarioSalario(request.POST['comentario'])
		salario.save()

		return HttpResponseRedirect(reverse('Inventory:salarioR'))
	else:
		return HttpResponse("Utilice el metodo POST")

#===============================================================================
#=========================       PROFESION  RRHH       =========================
#===============================================================================
@login_required()
def profesionR(request):
	profesion= Profesion.objects.all()
	empleado=Empleado.objects.all()
	gradoAcademico=GradoAcademico.objects.all()
	return render(request,'profesionR.html',{'profesion':profesion,'gradoAcademico':gradoAcademico,'empleado':empleado})

@login_required()
def editarprofesionR(request,id):
	editarprofesionR= Profesion.objects.get(pk=id)
	
	if request.method=='GET':
		form=ProfesionForm(instance=editarprofesionR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProfesionForm(request.POST,instance=editarprofesionR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:profesionR'))
	return render(request,'editarprofesionR.html',{'form':form})

@login_required()
def nuevoprofesionR(request):
	if request.method == 'POST' :
		profesion=Profesion()
		profesion.cod_empleado=Empleado(request.POST['empleado'])
		profesion.profesion=request.POST['profesion']
		profesion.gradoacademico=GradoAcademico(request.POST['gradoAcademico'])
		profesion.save()

		return	HttpResponseRedirect(reverse('Inventory:profesionR'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==============     CARGO     RRHH     ==========================
#================================================================
@login_required()
def cargoR(request):
	cargo= Cargo.objects.all()
	deptos=Departamento.objects.all()
	return render(request,'cargoR.html',{'cargo':cargo,'deptos':deptos})

@login_required()
def editarcargoR(request,id):
	editarcargoR= Cargo.objects.get(pk=id)
	
	if request.method=='GET':
		form=CargoForm(instance=editarcargoR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=CargoForm(request.POST,instance=editarcargoR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:cargoR'))
	return render(request,'editarcargoR.html',{'form':form})

@login_required()
def nuevocargoR(request):
	if request.method == 'POST' :
		cargo=Cargo()
		cargo.cargo=request.POST['cargo']
		cargo.departamento=Departamento(request.POST['deptos'])
		cargo.save()
		return HttpResponseRedirect(reverse('Inventory:cargoR'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============     DEPARTAMENTO     RRHH     ====================
#================================================================
@login_required()
def departamentoR(request):
	departamento= Departamento.objects.all()
	return render(request,'departamentoR.html',{'departamento':departamento})

@login_required()
def editardepartamentoR(request,id):
	editardepartamentoR= Departamento.objects.get(pk=id)
	

	if request.method=='GET':
		form=DepartamentoForm(instance=editardepartamentoR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DepartamentoForm(request.POST,instance=editardepartamentoR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:departamentoR'))
	return render(request,'editardepartamentoR.html',{'form':form})

@login_required()
def nuevodepartamentoR(request):
	if request.method == 'POST' :
		departamento=Departamento()
		departamento.departamento=request.POST['departamento']

		departamento.save()
		return HttpResponseRedirect(reverse('Inventory:departamentoR'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=================     REGIONAL     RRHH     ====================
#================================================================
@login_required()
def regionalR(request):
	regional= Regional.objects.all()
	return render(request,'regionalR.html',{'regional':regional})

@login_required()
def editarregionalR(request,id):
	editarregionalR= Regional.objects.get(pk=id)

	if request.method=='GET':
		form=RegionalForm(instance=editarregionalR)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=RegionalForm(request.POST,instance=editarregionalR)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:regionalR'))
	return render(request,'editarregionalR.html',{'form':form})

@login_required()
def nuevoregionalR(request):
	if request.method == 'POST' :
		regional=Regional()
		regional.regional=request.POST['regional']

		regional.save()
		return HttpResponseRedirect(reverse('Inventory:regionalR'))
	else:
		return HttpResponse("Utilice el metodo POST")

#=================================================================================
#********************************     COMPRAS     ********************************
#=================================================================================

#==================================================================
#================     PROVEEDOR    COMPRAS     ====================
#==================================================================
@login_required()
def proveedorC(request):
	proveedor= EmpresaProveedor.objects.all()
	return render(request,'proveedorC.html',{'proveedor':proveedor})

@login_required()
def editarproveedorC(request,id):
	editarproveedorC= EmpresaProveedor.objects.get(pk=id)

	if request.method=='GET':
		form=ProveedorForm(instance=editarproveedorC)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProveedorForm(request.POST,instance=editarproveedorC)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:proveedorC'))
	return render(request,'editarproveedorC.html',{'form':form})

@login_required()
def nuevoproveedorC(request):
	if request.method=='POST':
		proveedor=EmpresaProveedor()
		proveedor.RTN=request.POST['RTN']
		proveedor.nombre=request.POST['nombre']
		proveedor.correo=request.POST['correo']

		proveedor.save()
		return HttpResponseRedirect(reverse('Inventory:proveedorC'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============     TELEFONO PROVEEDOR COMPRAS     ===============
#================================================================
@login_required()
def telefonoproveedorC(request):
	telefonoproveedor= TelefonoProveedor.objects.all()
	proveedor=EmpresaProveedor.objects.all()
	return render(request,'telefonoproveedorC.html',{'telefonoproveedor':telefonoproveedor,'proveedor':proveedor})

@login_required()
def editartelefonoproveedorC(request,id):
	editartelefonoproveedorC= TelefonoProveedor.objects.get(pk=id)
	
	if request.method=='GET':
		form=TelefonoProveedorForm(instance=editartelefonoproveedorC)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=TelefonoProveedorForm(request.POST,instance=editartelefonoproveedorC)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoproveedorC'))
	return render(request,'editartelefonoproveedorC.html',{'form':form})

@login_required()
def nuevotelefonoproveedorC(request):
	if request.method == 'POST' :
		telefono=TelefonoProveedor()
		telefono.EmpresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		telefono.telefono=request.POST['telefono']
		telefono.Comentario=request.POST['comentario']

		telefono.save()
		return HttpResponseRedirect(reverse('Inventory:telefonoproveedorC'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminartelefonoproveedorC(request,id):
	telefono=TelefonoProveedor.objects.get(id=id);
	telefono.delete()
	return HttpResponseRedirect(reverse('Inventory:telefonoproveedorC'))

#================================================================
#=============     DIRECCION PROVEEDOR COMPRAS     ==============
#================================================================
@login_required()
def direccionproveedorC(request):
	direccionproveedor= DireccionProveedor.objects.all()
	proveedor=EmpresaProveedor.objects.all()
	return render(request,'direccionproveedorC.html',{'direccionproveedor':direccionproveedor,'proveedor':proveedor})

@login_required()
def editardireccionproveedorC(request,id):
	editardireccionproveedorC= DireccionProveedor.objects.get(pk=id)

	if request.method=='GET':
		form=DireccionProveedorForm(instance=editardireccionproveedorC)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=DireccionProveedorForm(request.POST,instance=editardireccionproveedorC)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:direccionproveedorC'))
	return render(request,'editardireccionproveedorC.html',{'form':form})

@login_required()
def nuevodireccionproveedorC(request):
	if request.method == 'POST' :
		direccion=DireccionProveedor()
		direccion.EmpresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		direccion.direccion=request.POST['direccion']
		direccion.Comentario=request.POST['comentario']

		direccion.save()
		return HttpResponseRedirect(reverse('Inventory:direccionproveedorC'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def eliminardireccionproveedorC(request,id):
	direccion=DireccionProveedor.objects.get(id=id);
	direccion.delete()
	return HttpResponseRedirect(reverse('Inventory:direccionproveedorC'))

#================================================================================
#********************     INFORMATICA  &  TECNOLOGIA     ************************
#================================================================================

#================================================================================
#===============================  EQUIPO  IT  ===================================
#================================================================================
@login_required()
def equipos(request):
	return render(request,'equiposIT.html')

@login_required()
def equipoIT(request):
	equipo=InventarioEquipo.objects.all()
	modelo=Modelo.objects.all()
	marca=Marca.objects.all()
	tipo=TipoEquipo.objects.filter(tipo="Laptop") | TipoEquipo.objects.filter(tipo="Desktop")
	sistema=SistemaOperativo.objects.all()
	disco=DiscoDuro.objects.all()
	ram=RAM.objects.all()
	procesador=Procesador.objects.all()
	regionales=Regional.objects.all()
	proveedores=EmpresaProveedor.objects.all()
	estados=EstadoEquipo.objects.all()

	data={
		'equipo':equipo,
		'modelo':modelo,
		'marca':marca,
		'tipo':tipo,
		'sistema':sistema,
		'disco':disco,
		'ram':ram,
		'procesador':procesador,
		'regionales':regionales,
		'proveedores':proveedores,
		'estados':estados,
	}
	return render(request,'equipoIT.html',data)

@login_required()
def editarequipoIT(request,id):
	editarequipo= InventarioEquipo.objects.get(pk=id)
	
	if request.method=='GET':
		form=EquipoForm(instance=editarequipo)
	else:
		form=EquipoForm(request.POST,instance=editarequipo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:equipoIT'))
	return render(request,'editarequipoIT.html',{'form':form})

@login_required()
def nuevoequipoIT(request):
	if request.method == 'POST' :
		equipo=InventarioEquipo()
		equipo.codigo_Inventario=request.POST['codInventario']
		equipo.codigo_equipo=request.POST['codEquipo']
		equipo.tipo=TipoEquipo(request.POST['tipo'])
		equipo.sistema=SistemaOperativo(request.POST['sistema'])
		equipo.disco=DiscoDuro(request.POST['disco'])
		equipo.ram=RAM(request.POST['ram'])
		equipo.procesador=Procesador(request.POST['procesador'])
		equipo.marca=Marca(request.POST['marca'])
		equipo.modelo=Modelo(request.POST['modelo'])
		equipo.descripcion=request.POST['descripcion']
		equipo.serial=request.POST['serial']
		equipo.n_orden_compra=request.POST['ordencompra']
		equipo.empresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		equipo.regional=Regional(request.POST['regional'])
		equipo.estado_equipo=EstadoEquipo(request.POST['estado'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:equipoIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#======================================================================================		
#=========================  INVENTARIO IMPRESORAS  & MAS IT  ==========================
#======================================================================================

@login_required()
def impresorasIT(request):
	equipo=OtroInventario.objects.all()
	modelo=Modelo.objects.all()
	marca=Marca.objects.all()
	tipo=TipoEquipo.objects.all()
	regionales=Regional.objects.all()
	empleado=Empleado.objects.all()
	proveedores=EmpresaProveedor.objects.all()
	estados=EstadoEquipo.objects.all()

	data={
		'equipo':equipo,
		'regionales':regionales,
		'proveedores':proveedores,
		'estados':estados,
		'modelo':modelo,
		'marca':marca,
		'tipo':tipo,
		'empleado':empleado,
	}
	return render(request,'impresorasIT.html',data)

@login_required()
def editarimpresorasIT(request,id):
	editarimpresoras= OtroInventario.objects.get(pk=id)
	
	if request.method=='GET':
		form=ImpresorasForm(instance=editarimpresoras)
	else:
		form=ImpresorasForm(request.POST,instance=editarimpresoras)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:impresorasIT'))
	return render(request,'editarimpresorasIT.html',{'form':form})

@login_required()
def nuevoimpresorasIT(request):
	if request.method == 'POST' :
		equipo=OtroInventario()
		equipo.codigo_Inventario=request.POST['codInventario']
		equipo.tipo=TipoEquipo(request.POST['tipo'])
		equipo.marca=Marca(request.POST['marca'])
		equipo.modelo=Modelo(request.POST['modelo'])
		equipo.serial=request.POST['serial']
		equipo.n_orden_compra=request.POST['ordencompra']
		equipo.descripcion=request.POST['descripcion']
		equipo.empresaProveedor=EmpresaProveedor(request.POST['proveedor'])
		equipo.empleado=Empleado(request.POST['empleado'])
		equipo.regional=Regional(request.POST['regional'])
		equipo.estado="True"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:impresorasIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============     ASIGNACION     IT     ========================
#================================================================
@login_required()
def asignaciones(request):
	return render(request,'asignaciones.html')


@login_required()
def asignacionIT(request):
	asignacion=Asignacion.objects.all()
	equipos = InventarioEquipo.objects.filter(estado="False")
	estadoAsignacion= Asignacion.objects.filter(estadoAsignacion="True")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'asignacionIT.html',{'estadoAsignacion':estadoAsignacion,'asignacion':asignacion,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editarasignacionIT(request,id):
	editarasignacionIT= Asignacion.objects.get(pk=id)
	
	if request.method=='GET':
		form=AsignacionForm(instance=editarasignacionIT)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=AsignacionForm(request.POST,instance=editarasignacionIT)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:asignacionIT'))
	return render(request,'editarasignacionIT.html',{'form':form})

@login_required()
def nuevoasignacionIT(request):
	if request.method == 'POST' :
		asignacion=Asignacion()
		asignacion.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		asignacion.cod_empleadoRecibe=Empleado(request.POST['CodEmpleadoRecibe'])
		asignacion.cod_empleadoEntrega=Empleado(request.POST['CodEmpleadoEntrega'])
		asignacion.Comentario=request.POST['Comentario']
		asignacion.estadoAsignacion="True"
		asignacion.save()

		equipo=InventarioEquipo.objects.get(pk=request.POST['CodEquipo'])
		equipo.estado="True"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:asignacionIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============   ASIGNACION IMPRESORAS  IT=======================
#================================================================
@login_required()
def asignacionImpresorasIT(request):
	asignacion=AsignacionImpresoras.objects.all()
	estado=EstadoEquipo.objects.filter(estado_equipo="Disponible")
	equipos = OtroInventario.objects.filter(estado="False" , estado_equipo=estado)
	estadoAsignacion= AsignacionImpresoras.objects.filter(estadoAsignacion="True")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'asignacionImpresorasIT.html',{'estadoAsignacion':estadoAsignacion,'asignacion':asignacion,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editarasignacionImpresorasIT(request,id):
	editarasignacion= AsignacionImpresoras.objects.get(pk=id)
	
	if request.method=='GET':
		form=AsignacionImpresorasForm(instance=editarasignacion)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=AsignacionImpresorasForm(request.POST,instance=editarasignacion)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:asignacionImpresorasIT'))
	return render(request,'editarasignacionImpresoraIT.html',{'form':form})

@login_required()
def nuevoasignacionImpresorasIT(request):
	if request.method == 'GET' :
		asignacion=AsignacionImpresoras()
		asignacion.codigo_Inventario=OtroInventario(request.GET.get("selectCodEquipo"))
		asignacion.cod_empleadoRecibe=Empleado(request.GET.get("selectEmpleadoRecibe"))
		asignacion.cod_empleadoEntrega=Empleado(request.GET.get("selectEmpleadoEntrega"))
		asignacion.Comentario=request.GET.get('Comentario')
		asignacion.estadoAsignacion="True"
		asignacion.save()
		equipo=OtroInventario.objects.get(pk=request.GET.get("selectCodEquipo"))
		equipo.estado="True"
		equipo.save()

		ctx={
			'Hola':'Hola'
		}
		return JsonResponse(ctx,safe=False)
	else:
		return JsonResponse(ctx,safe=False)


#================================================================
#==================== DESCARGO  IT ==============================
#================================================================
@login_required()
def descargos(request):
	return render(request,'descargos.html')

@login_required()
def descargoIT(request):
	descargo=Asignacion.objects.all()
	equipos = InventarioEquipo.objects.filter(estado="True")
	estadoAsignacion= Asignacion.objects.filter(estadoAsignacion="False")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)

	return render(request,'descargoIT.html',{'estadoAsignacion':estadoAsignacion,'descargo':descargo,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def nuevodescargoIT(request):
	if request.method == 'POST' :
		descargo=Asignacion()
		descargo.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		descargo.cod_empleadoRecibe=Empleado(request.POST['CodEmpleadoRecibe'])
		descargo.cod_empleadoEntrega=Empleado(request.POST['idEntrega'])
		descargo.Comentario=request.POST['Comentario']
		descargo.estadoAsignacion="False"
		descargo.save()

		equipo=InventarioEquipo.objects.get(pk=request.POST['CodEquipo'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:descargoIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def EntregadescargoIT(request,pk):	
	empleado=Asignacion.objects.filter(codigo_equipo= pk, estadoAsignacion='True').values('cod_empleadoRecibe')
	lista=empleado.latest('cod_empleadoRecibe') 

	return JsonResponse(lista,safe=False)

@login_required()
def EmpleadoEntregaIT(request,pk):	
	empleado=Empleado.objects.filter(pk= pk).values('primer_nombre','primer_apellido')
	lista=empleado.latest('primer_nombre') 

	return JsonResponse(lista,safe=False)

#================================================================
#==================== DESCARGO  IMPRESORAS  IT  =================
#================================================================

@login_required()
def descargoImpresorasIT(request):
	descargo=AsignacionImpresoras.objects.all()
	equipos = OtroInventario.objects.filter(estado="True")
	estadoAsignacion= AsignacionImpresoras.objects.filter(estadoAsignacion="False")

	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	empleados=Empleado.objects.all()
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id==cargo.id:
				listaEmpleados.append(empleado)

	return render(request,'descargoImpresorasIT.html',{'estadoAsignacion':estadoAsignacion,'descargo':descargo,'equipos':equipos,'empleados':empleados,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def nuevodescargoImpresorasIT(request):
	if request.method == 'POST' :
		descargo=AsignacionImpresoras()
		descargo.codigo_Inventario=OtroInventario(request.POST['CodEquipo'])
		descargo.cod_empleadoRecibe=Empleado(request.POST['CodEmpleadoRecibe'])
		descargo.cod_empleadoEntrega=Empleado(request.POST['idEntrega'])
		descargo.Comentario=request.POST['Comentario']
		descargo.estadoAsignacion="False"
		descargo.save()

		equipo=OtroInventario.objects.get(pk=request.POST['CodEquipo'])
		equipo.estado="False"
		equipo.save()

		return HttpResponseRedirect(reverse('Inventory:descargoImpresorasIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

@login_required()
def EntregadescargoImpresorasIT(request,pk):	
	empleado=AsignacionImpresoras.objects.filter(codigo_Inventario= pk, estadoAsignacion='True').values('cod_empleadoRecibe')
	lista=empleado.latest('cod_empleadoRecibe') 

	return JsonResponse(lista,safe=False)

@login_required()
def EmpleadoEntregaImpresorasIT(request,pk):	
	empleado=Empleado.objects.filter(pk= pk).values('primer_nombre','primer_apellido')
	lista=empleado.latest('primer_nombre') 

	return JsonResponse(lista,safe=False)

#================================================================
#=============     MANTENIMIENTO     IT    ======================
#================================================================
@login_required()
def mantenimientosdeequipo(request):
	return render(request,'mantenimientosdeequipo.html')

@login_required()
def mantenimientoIT(request):
	mantenimiento= Mantenimiento.objects.all()
	equipos=InventarioEquipo.objects.all()
	empleados=Empleado.objects.all()
	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id== cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'mantenimientoIT.html',{'mantenimiento':mantenimiento,'empleados':empleados,'equipos':equipos,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editarmantenimientoIT(request,id):
	editarmantenimientoIT= Mantenimiento.objects.get(pk=id)

	if request.method=='GET':
		form=MantenimientoForm(instance=editarmantenimientoIT)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MantenimientoForm(request.POST,instance=editarmantenimientoIT)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimientoIT'))
	return render(request,'editarmantenimientoIT.html',{'form':form})

@login_required()
def nuevomantenimientoIT(request):
	if request.method == 'POST' :
		mantenimiento=Mantenimiento()
		mantenimiento.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		mantenimiento.causa_Falla=request.POST['causa']
		mantenimiento.accion_Realizar=request.POST['realizar']
		mantenimiento.fecha_salida=request.POST['fechaSalida']
		mantenimiento.cod_empleado=Empleado(request.POST['CodEmpleado'])
		mantenimiento.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimientoIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============MANTENIMIENTO de Impresoras IT=====================
#================================================================
@login_required()
def mantenimientoImpresoraIT(request):
	mantenimiento= OtroMantenimiento.objects.all()
	equipos=OtroInventario.objects.all()
	proveedor=EmpresaProveedor.objects.all()
	empleados=Empleado.objects.all()
	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id== cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'mantenimientoImpresoraIT.html',{'mantenimiento':mantenimiento,'proveedor':proveedor,'empleados':empleados,'equipos':equipos,'departamento':departamento,'cargos':cargos,'listaEmpleados':listaEmpleados})

@login_required()
def editarmantenimientoImpresoraIT(request,id):
	editarmantenimientoImpresora= OtroMantenimiento.objects.get(pk=id)

	if request.method=='GET':
		form=MantenimientoImpresorasForm(instance=editarmantenimientoImpresora)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MantenimientoImpresorasForm(request.POST,instance=editarmantenimientoImpresora)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimientoImpresoraIT'))
	return render(request,'editarotromantenimientoIT.html',{'form':form})

@login_required()
def nuevomantenimientoImpresoraIT(request):
	if request.method == 'POST' :
		mantenimiento=OtroMantenimiento()
		mantenimiento.codigo_Inventario=OtroInventario(request.POST['CodInventario'])
		mantenimiento.causa_Falla=request.POST['causa']
		mantenimiento.accion_Realizar=request.POST['realizar']
		mantenimiento.fecha_salida=request.POST['fechaSalida']
		mantenimiento.proveedor=EmpresaProveedor(request.POST['Codproveedor'])
		mantenimiento.cod_empleado=Empleado(request.POST['CodEmpleado'])
		mantenimiento.save()
		return HttpResponseRedirect(reverse('Inventory:mantenimientoImpresoraIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#=============================================================================================
#=======================================HERRAMIENTAS==========================================
#=============================================================================================
@login_required()
def herramientasIT(request):
	return render(request,'herramientasIT.html')

#================================================================
#=================== Tipo EQUIPO IT ================================
#================================================================
@login_required()
def tipoEquipoIT(request):
	tipo= TipoEquipo.objects.all()
	return render(request,'tipoEquipoIT.html',{'tipo':tipo})

@login_required()
def editartipoEquipoIT(request,id):
	editartipoEquipo=TipoEquipo.objects.get(pk=id)

	if request.method=='GET':
		form=tipoEquipoForm(instance=editartipoEquipo)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=tipoEquipoForm(request.POST,instance=editartipoEquipo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:tipoEquipoIT'))
	return render(request,'editartipoEquipoIT.html',{'form':form})

@login_required()
def nuevotipoEquipoIT(request):
	if request.method == 'POST' :
		tipo=TipoEquipo()
		tipo.tipo=request.POST['tipo']

		tipo.save()
		return HttpResponseRedirect(reverse('Inventory:tipoEquipoIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#================== MARCA DE EQUIPO =============================
#================================================================
@login_required()
def marcaIT(request):
	marca= Marca.objects.all()
	tipo=TipoEquipo.objects.all()
	return render(request,'marcaIT.html',{'marca':marca,'tipo':tipo})

@login_required()
def editarmarcaIT(request,id):
	editarmarca=Marca.objects.get(pk=id)

	if request.method=='GET':
		form=MarcaForm(instance=editarmarca)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=MarcaForm(request.POST,instance=editarmarca)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:marcaIT'))
	return render(request,'editarmarcaIT.html',{'form':form})

@login_required()
def nuevomarcaIT(request):
	if request.method == 'POST' :
		marca=Marca()
		marca.marca=request.POST['marca']
		marca.tipo=TipoEquipo(request.POST['tipo'])
		marca.save()
		return HttpResponseRedirect(reverse('Inventory:marcaIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#=================================================================
#=============        MODELO              ========================
#=================================================================
@login_required()
def modeloIT(request):
	modelo= Modelo.objects.all()
	marca=Marca.objects.all()
	return render(request,'modeloIT.html',{'modelo':modelo,'marca':marca})

@login_required()
def editarmodeloIT(request,id):
	editarmodelo= Modelo.objects.get(pk=id)

	if request.method=='GET':
		form=ModeloForm(instance=editarmodelo)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ModeloForm(request.POST,instance=editarmodelo)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:modeloIT'))
	return render(request,'editarmodeloIT.html',{'form':form})

@login_required()
def nuevomodeloIT(request):
	if request.method == 'POST' :
		modelo=Modelo()
		modelo.marca=Marca(request.POST['marca'])
		modelo.modelo=request.POST['modelo']
		modelo.save()

		return	HttpResponseRedirect(reverse('Inventory:modeloIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#============= SISTEMA OPERATIVO ================================
#================================================================
@login_required()
def sistemaIT(request):
	sistema= SistemaOperativo.objects.all()
	return render(request,'sistemaIT.html',{'sistema':sistema})

@login_required()
def editarsistemaIT(request,id):
	editarsistema=SistemaOperativo.objects.get(pk=id)

	if request.method=='GET':
		form=SistemaForm(instance=editarsistema)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=SistemaForm(request.POST,instance=editarsistema)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:sistemaIT'))
	return render(request,'editarsistemaIT.html',{'form':form})

@login_required()
def nuevosistemaIT(request):
	if request.method == 'POST' :
		sistema=SistemaOperativo()
		sistema.sistema=request.POST['sistema']

		sistema.save()
		return HttpResponseRedirect(reverse('Inventory:sistemaIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==================== DISCO DURO ================================
#================================================================
@login_required()
def discoDuroIT(request):
	disco= DiscoDuro.objects.all()
	return render(request,'discoDuroIT.html',{'disco':disco})

@login_required()
def editardiscoDuroIT(request,id):
	editardiscoDuro=DiscoDuro.objects.get(pk=id)

	if request.method=='GET':
		form=discoDuroForm(instance=editardiscoDuro)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=discoDuroForm(request.POST,instance=editardiscoDuro)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:discoDuroIT'))
	return render(request,'editardiscoDuroIT.html',{'form':form})

@login_required()
def nuevodiscoDuroIT(request):
	if request.method == 'POST' :
		discoDuro=DiscoDuro()
		discoDuro.disco=request.POST['discoDuro']

		discoDuro.save()
		return HttpResponseRedirect(reverse('Inventory:discoDuroIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==================== MEMORIA RAM================================
#================================================================
@login_required()
def memoriaRAMIT(request):
	rams= RAM.objects.all()
	return render(request,'RAMIT.html',{'rams':rams})

@login_required()
def editarmemoriaRAMIT(request,id):
	editarRAM=RAM.objects.get(pk=id)

	if request.method=='GET':
		form=RAMForm(instance=editarRAM)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=RAMForm(request.POST,instance=editarRAM)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:memoriaRAMIT'))
	return render(request,'editarRAMIT.html',{'form':form})

@login_required()
def nuevomemoriaRAMIT(request):
	if request.method == 'POST' :
		ram=RAM()
		ram.ram=request.POST['memoriaRAM']

		ram.save()
		return HttpResponseRedirect(reverse('Inventory:memoriaRAMIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#==================== PROCESADOR ================================
#================================================================
@login_required()
def procesadorIT(request):
	procesador= Procesador.objects.all()
	return render(request,'procesadorIT.html',{'procesador':procesador})

@login_required()
def editarprocesadorIT(request,id):
	editarprocesador=Procesador.objects.get(pk=id)

	if request.method=='GET':
		form=ProcesadorForm(instance=editarprocesador)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=ProcesadorForm(request.POST,instance=editarprocesador)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:procesadorIT'))
	return render(request,'editarprocesadorIT.html',{'form':form})

@login_required()
def nuevoprocesadorIT(request):
	if request.method == 'POST' :
		procesador=Procesador()
		procesador.procesador=request.POST['procesador']

		procesador.save()
		return HttpResponseRedirect(reverse('Inventory:procesadorIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#================================================================
#=============     GARANTIA   IT     ============================
#================================================================
@login_required()
def garantiaIT(request):
	garantia= Garantia.objects.all()
	equipo=InventarioEquipo.objects.all()
	empleados=Empleado.objects.all()
	departamento=Departamento.objects.get(departamento="Informatica & Tecnologia")
	cargos=Cargo.objects.filter(departamento=departamento)
	listaEmpleados=[]
	for empleado in empleados:
		for cargo in cargos:
			if empleado.cargo.id== cargo.id:
				listaEmpleados.append(empleado)
	return render(request,'garantiaIT.html',{'garantia':garantia,'empleados':empleados,'equipo':equipo,'departamento':departamento,'cargo':cargo,'listaEmpleados':listaEmpleados})

@login_required()
def editargarantiaIT(request,id):
	editargarantia= Garantia.objects.get(pk=id)
	
	if request.method=='GET':
		form=GarantiaForm(instance=editargarantia)
		for field in form.fields:
			form.fields[field].widget.attrs['class']='form-control'
	else:
		form=GarantiaForm(request.POST,instance=editargarantia)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse('Inventory:garantiaIT'))
	return render(request,'editargarantiaIT.html',{'form':form})

@login_required()
def nuevogarantiaIT(request):
	if request.method == 'POST' :
		garantia=Garantia()
		garantia.N_Caso=request.POST['caso']
		garantia.codigo_equipo=InventarioEquipo(request.POST['CodEquipo'])
		garantia.Asunto=request.POST['asunto']
		garantia.Fecha_aperturaCaso=request.POST['fechaApertura']
		garantia.Fecha_entregaProducto=request.POST['fechaEntrega']
		garantia.cod_empleado=Empleado(request.POST['CodEmpleado'])

		garantia.save()
		return HttpResponseRedirect(reverse('Inventory:garantiaIT'))
	else:
		return HttpResponse("Utilice el metodo POST")

#===============================================================================================================
#===============================================================================================================
#=========================   REPORTES      REPORTES   ADMIN   ==================================================
#===============================================================================================================
#===============================================================================================================
#===============================================================================================================

@login_required
def reportesGenerales(request):
	return render(request,'adminREPORTES.HTML')

@login_required
def reportesAsignacion(request):
	return render(request,'asigREPORTES.HTML')

# class EmpleadoPdfView(PdfMixin, ListView):
# 	model = Empleado
# 	template_name = 'empleado_pdf.html'

@login_required
def empleadopdf(request):
	cod_empleado  = Empleado.objects.all()
	telefono  = TelefonoEmpleado.objects.filter(cod_empleado=cod_empleado)
	direccion = DireccionEmpleado.objects.filter(Empleado=cod_empleado)

	data={
		'cod_empleado':cod_empleado,
		'telefono':telefono,
	 	'direccion':direccion,
	}

	return render(request, 'empleado_pdf.html', data)

# class InforEmpleadoPdfView(PdfMixin, ListView):
# 	model = Empleado
# 	template_name = 'empleado_pdf.html'

@login_required
def inforempleadopdf(request,id):
	cod_empleado=Empleado.objects.get(pk=id)
	telefono=TelefonoEmpleado.objects.filter(cod_empleado=cod_empleado)
	direccion=DireccionEmpleado.objects.filter(Empleado=cod_empleado)
	profesion=Profesion.objects.filter(cod_empleado=cod_empleado)
	contrato=Contrato.objects.filter(cod_empleado=cod_empleado)
	asignacion=Asignacion.objects.filter(cod_empleadoRecibe=cod_empleado)
	salario=Salario.objects.filter(contrato=contrato)

	data={
		'cod_empleado':cod_empleado,
	 	'telefono':telefono,
	 	'direccion':direccion,
		'profesion':profesion,	
		'contrato':contrato,
		'asignacion':asignacion,
		'salario':salario,
	}

	return render(request,'inforEmpleado_pdf.html', data)

@login_required
def empleadoAsignacion(request,id):
	empleado=Empleado.objects.get(pk=id)
	asignacion=Asignacion.objects.filter(cod_empleadoRecibe=empleado) | Asignacion.objects.filter(cod_empleadoEntrega=empleado)

	data={
		'empleado':empleado,
		'asignacion':asignacion,
	}

	return render(request,'historialequipoEmpleado.html', data)

# class EquipoPdfView(PdfMixin, ListView):
# 	model = Empleado
# 	template_name = 'empleado_pdf.html'

@login_required
def equipopdf(request):
	equipo = InventarioEquipo.objects.all()
	return render(request, 'equipo_pdf.html', {'object_list': equipo})

@login_required
def impresoraspdf(request):
	impresoras = OtroInventario.objects.all()
	return render(request, 'impresoraspdf.html', {'object_list': impresoras})


@login_required()
def historialequipo(request,id):
	codigo_equipo=InventarioEquipo.objects.get(pk=id)
	asignacion=Asignacion.objects.filter(codigo_equipo=codigo_equipo)
	estadoAsignacion= Asignacion.objects.filter(estadoAsignacion="True")
	estadoDescargo=Asignacion.objects.filter(estadoAsignacion="False")
	garantia=Garantia.objects.filter(codigo_equipo=codigo_equipo)
	mantenimiento=Mantenimiento.objects.filter(codigo_equipo=codigo_equipo)

	data={
		'codigo_equipo':codigo_equipo,
	 	'asignacion':asignacion,
	 	'garantia':garantia,
	 	'mantenimiento':mantenimiento,
	 	'estadoAsignacion':estadoAsignacion,
	 	'estadoDescargo':estadoDescargo,
	}

	return render(request, 'historialequipo.html',data)

@login_required()
def historialimpresoras(request,id):
	codigo_Inventario=OtroInventario.objects.get(pk=id)
	asignacion=AsignacionImpresoras.objects.filter(codigo_Inventario=codigo_Inventario)
	estadoAsignacion= AsignacionImpresoras.objects.filter(estadoAsignacion="True")
	estadoDescargo=Asignacion.objects.filter(estadoAsignacion="False")
	mantenimiento=OtroMantenimiento.objects.filter(codigo_Inventario=codigo_Inventario)

	data={
		'codigo_Inventario':codigo_Inventario,
	 	'mantenimiento':mantenimiento,
	 	'asignacion':asignacion,
		'estadoAsignacion':estadoAsignacion,
	 	'estadoDescargo':estadoDescargo,
	}

	return render(request, 'historialimpresoras.html',data)

# class AsignacionPdfView(PdfMixin, ListView):
# 	model = Asignacion
# 	template_name = 'asignacion_pdf.html'

@login_required
def asignacionpdf(request):
	asignacion = Asignacion.objects.all()
	return render(request, 'asignacion_pdf.html', {'object_list': asignacion})

# class ProveedorPdfView(PdfMixin, ListView):
# 	model = Empleado
# 	template_name = 'proveedor_pdf.html'

@login_required
def proveedorpdf(request):
	proveedor = EmpresaProveedor.objects.all()
	telefono  = TelefonoProveedor.objects.filter(EmpresaProveedor=proveedor)
	direccion = DireccionProveedor.objects.filter(EmpresaProveedor=proveedor)

	data={
		'proveedor':proveedor,
		'telefono':telefono,
		'direccion':direccion,
	}
	return render(request, 'proveedor_pdf.html', data)

@login_required
def mantenimientopdf(request):
	mantenimiento = Mantenimiento.objects.all()
	return render(request, 'mantenimiento_pdf.html', {'object_list': mantenimiento})

@login_required
def otrosmantenimientopdf(request):
	mantenimiento = OtroMantenimiento.objects.all()
	return render(request, 'otrosMantenimientos_pdf.html', {'object_list': mantenimiento})