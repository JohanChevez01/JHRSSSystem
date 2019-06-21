from django.forms import ModelForm 
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
	class Meta:
		model =User
		fields= ['username','first_name', 'last_name', 'password1', 'password2']

class EmpleadoForm(ModelForm):
	class Meta:
		model = Empleado
		fields= '__all__'
	def __init__(self, *args, **kwargs):
	    super(EmpleadoForm, self).__init__(*args, **kwargs)
	    for campo in self.fields:
		    self.fields['cod_empleado'].widget.attrs['class']='form-control'
		    self.fields['cod_empleado'].label='Codigo Empleado'
		    self.fields['identidad'].widget.attrs['data-mask']='9999-9999-99999'
		    self.fields['identidad'].label='Identidad'
		    self.fields['identidad'].widget.attrs['class']='form-control'
		    self.fields['primer_nombre'].widget.attrs['class']='form-control'
		    self.fields['segundo_nombre'].widget.attrs['class']='form-control'
		    self.fields['primer_apellido'].widget.attrs['class']='form-control'
		    self.fields['segundo_apellido'].widget.attrs['class']='form-control'
		    self.fields['fechanacimiento'].widget.attrs['size'] = '10'
		    self.fields['fechanacimiento'].label='Fecha Nacimiento'
		    self.fields['fechanacimiento'].widget.attrs['class']='form-control'
		    self.fields['genero'].choices = [('', 'Seleccione Genero')] + list(self.fields['genero'].choices)[1:]
		    self.fields['genero'].widget.attrs['class']='form-control'
		    self.fields['estadocivil'].choices = [('', 'Seleccione Estado Civil')] + list(self.fields['estadocivil'].choices)[1:]
		    self.fields['estadocivil'].label='Estado Civil'
		    self.fields['estadocivil'].widget.attrs['class']='form-control'
		    self.fields['cargo'].choices = [('', 'Seleccione Cargo')] + list(self.fields['cargo'].choices)[1:]
		    self.fields['cargo'].widget.attrs['class']='form-control'
		    self.fields['regional'].choices = [('', 'Seleccione Regional')] + list(self.fields['regional'].choices)[1:]
		    self.fields['regional'].widget.attrs['class']='form-control'
		    self.fields['user'].choices = [('', 'Seleccione Usuario')] + list(self.fields['user'].choices)[1:]
		    self.fields['user'].label='Usuario'
		    self.fields['user'].widget.attrs['class']='form-control'
		    self.fields['correo'].widget.attrs['class']='form-control'
		    self.fields.get('estado').widget.attrs['class']='form-control'

class TelefonoEmpleadoForm(ModelForm):
	class Meta:
		model = TelefonoEmpleado
		fields= '__all__'
	def __init__(self, *args, **kwargs):
	    super(TelefonoEmpleadoForm, self).__init__(*args, **kwargs)
	    for campo in self.fields:
	    	self.fields['cod_empleado'].choices =[('','seleccione empleado')]+list(self.fields['cod_empleado'].choices)[1:]
	    	self.fields['cod_empleado'].label='Codigo Empleado'
	    	# self.fields.get('empleador').widget=forms.HiddenInput()
	    	self.fields['telefono'].label = 'Telefono'
	    	self.fields['telefono'].widget.attrs['data-mask']='9999-9999'
	    	self.fields['Comentario'].choices=[('','Seleccione Comentario Telefonico')]+ list(self.fields['Comentario'].choices)[1:]

class DireccionEmpleadoForm(ModelForm):
	class Meta:
		model = DireccionEmpleado
		fields= '__all__'
	def __init__(self, *args, **kwargs):
	    super(DireccionEmpleadoForm, self).__init__(*args, **kwargs)
	    for campo in self.fields:
	    	self.fields['Empleado'].choices =[('','seleccione empleado')]+list(self.fields['Empleado'].choices)[1:]
	    	self.fields['Empleado'].label='Codigo Empleado'
	    	self.fields['direccion'].label='Direccion'
	    	self.fields['Comentario'].choices=[('','Seleccione Comentario Direccion')]+ list(self.fields['Comentario'].choices)[1:]

class ContratoForm(ModelForm):
	class Meta:
		model = Contrato
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(ContratoForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['cod_empleado'].choices=[('','Seleccione empleado')]+list(self.fields['cod_empleado'].choices)[1:]
			self.fields ['cod_empleado'].label='Codigo Empleado'
			self.fields ['fecha_inicio'].widget.attrs['size']='10'
			self.fields ['fecha_inicio'].label='Fecha de Inicio'
			self.fields ['fecha_final'].widget.attrs['size']='10'
			self.fields ['fecha_final'].label='Fecha de Final'

class SalarioForm(ModelForm):
	class Meta:
		model = Salario
		fields= '__all__'
	def __init__(self, *args, **kwargs):
	    super(SalarioForm, self).__init__(*args, **kwargs)
	    for campo in self.fields:
	    	self.fields ['contrato'].choices=[('','Selecione el contrato')]+list(self.fields['contrato'].choices)[1:]
	    	self.fields ['contrato'].label='Numero de Contrato'
	    	self.fields ['salario'].widget.attrs['class']='form-control'
	    	self.fields ['fechaS'].widget.attrs['size']='10'
	    	self.fields ['fechaS'].label='Fecha Asignacion de Salario'
	    	self.fields ['comentarioSalario'].choices=[('','Selecione Motivo de Salario')]+list(self.fields['comentarioSalario'].choices)[1:]
	    	self.fields ['comentarioSalario'].label='Motivo de Contrato'

class ProfesionForm(ModelForm):
	class Meta:
		model = Profesion
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(ProfesionForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['cod_empleado'].label='Codigo Empleado'
			self.fields ['cod_empleado'].choices=[('','Seleccione Empleado')] + list(self.fields['cod_empleado'].choices)[1:]
			self.fields [campo].widget.attrs['class']='form-control'
			self.fields ['gradoacademico'].choices=[('','Seleccione Grado Academico')]+ list(self.fields['gradoacademico'].choices)[1:]
			self.fields ['gradoacademico'].label='Nivel de Grado Academico'

class CargoForm(ModelForm):
	class Meta:
		model = Cargo
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(CargoForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['cargo'].widget.attrs['class']='form-control'
			self.fields ['departamento'].choices = [('', 'Seleccione departamento')] + list(self.fields['departamento'].choices)[1:]

class DepartamentoForm(ModelForm):
	class Meta:
		model = Departamento
		fields= '__all__'
	def __init__ (self,*args,**kwargs):
		super(DepartamentoForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields [campo].widget.attrs['class'] = 'form-control'

class RegionalForm(ModelForm):
	class Meta:
		model = Regional
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(RegionalForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields [campo].widget.attrs['class']= 'form-control'

class EquipoForm(ModelForm):
	class Meta:
		model = InventarioEquipo
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(EquipoForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['codigo_Inventario'].widget.attrs['class']='form-control'
			self.fields ['codigo_Inventario'].label='Codigo Equipo'
			self.fields ['codigo_equipo'].widget.attrs['class']='form-control'
			self.fields ['codigo_equipo'].label='Codigo Equipo'
			# self.fields ['modelo.marca.tipo'].choices = [('','Seleccione Tipo')] + list(self.fields['tipo'].choices)[1:]
			# self.fields ['modelo.marca.tipo'].label='Tipo Equipo'
			# self.fields ['modelo.marca.tipo'].widget.attrs['class']='form-control'
			# self.fields ['marca'].choices = [('','Seleccione Marca')] + list(self.fields['modelo.marca'].choices)[1:]
			# self.fields ['marca'].label='Marca'
			# self.fields ['marca'].widget.attrs['class']='form-control'
			self.fields ['modelo'].choices = [('','Seleccione Modelo')] + list(self.fields['modelo'].choices)[1:]
			self.fields ['modelo'].label='Modelo'
			self.fields ['modelo'].widget.attrs['class']='form-control'
			self.fields ['sistema'].choices = [('','Seleccione Sistema Operativo')] + list(self.fields['sistema'].choices)[1:]
			self.fields ['sistema'].label='Sistema Operativo'
			self.fields ['sistema'].widget.attrs['class']='form-control'
			self.fields ['disco'].choices = [('','Seleccione Disco Duro')] + list(self.fields['disco'].choices)[1:]
			self.fields ['disco'].label='Disco Duro'
			self.fields ['disco'].widget.attrs['class']='form-control'
			self.fields ['ram'].choices = [('','Seleccione Memoria RAM')] + list(self.fields['ram'].choices)[1:]
			self.fields ['ram'].label='Memoria RAM'
			self.fields ['ram'].widget.attrs['class']='form-control'
			self.fields ['procesador'].choices = [('','Seleccione Procesador')] + list(self.fields['procesador'].choices)[1:]
			self.fields ['procesador'].label='Procesador'
			self.fields ['procesador'].widget.attrs['class']='form-control'
			self.fields ['serial'].widget.attrs['class']='form-control'
			self.fields ['n_orden_compra'].widget.attrs['class']='form-control'
			self.fields ['n_orden_compra'].label='N de Orden de Compra'
			self.fields ['descripcion'].widget.attrs['class']='form-control'
			self.fields ['empresaProveedor'].choices = [('','Seleccione Proveedor')] + list(self.fields['empresaProveedor'].choices)[1:]
			self.fields ['empresaProveedor'].label='Nombre del Proveedor'
			self.fields ['empresaProveedor'].widget.attrs['class']='form-control'
			self.fields ['regional'].choices = [('','Seleccione regional')] + list(self.fields['regional'].choices)[1:]
			self.fields ['regional'].label='Regional'
			self.fields ['regional'].widget.attrs['class']='form-control'
			self.fields ['estado_equipo'].choices = [('','Seleccione Estado Equipo')] + list(self.fields['estado_equipo'].choices)[1:]
			self.fields ['estado_equipo'].label='Estado Equipo'
			self.fields ['estado_equipo'].widget.attrs['class']='form-control'
			
class ImpresorasForm(ModelForm):
	class Meta:
		model = OtroInventario
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(ImpresorasForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['codigo_Inventario'].widget.attrs['class']='form-control'
			self.fields ['codigo_Inventario'].label='Codigo Inventario'
			# self.fields ['tipo'].choices = [('','Seleccione Tipo')] + list(self.fields['tipo'].choices)[1:]
			# self.fields ['tipo'].label='Tipo Equipo'
			# self.fields ['tipo'].widget.attrs['class']='form-control'
			# self.fields ['marca'].choices = [('','Seleccione Marca')] + list(self.fields['modelo.marca'].choices)[1:]
			# self.fields ['marca'].label='Marca'
			# self.fields ['marca'].widget.attrs['class']='form-control'
			self.fields ['modelo'].choices = [('','Seleccione Modelo')] + list(self.fields['modelo'].choices)[1:]
			self.fields ['modelo'].label='Modelo'
			self.fields ['modelo'].widget.attrs['class']='form-control'
			self.fields ['serial'].widget.attrs['class']='form-control'
			self.fields ['n_orden_compra'].widget.attrs['class']='form-control'
			self.fields ['n_orden_compra'].label='N de Orden de Compra'
			self.fields ['descripcion'].widget.attrs['class']='form-control'
			self.fields ['empresaProveedor'].choices = [('','Seleccione Proveedor')] + list(self.fields['empresaProveedor'].choices)[1:]
			self.fields ['empresaProveedor'].label='Nombre del Proveedor'
			self.fields ['empresaProveedor'].widget.attrs['class']='form-control'
			self.fields ['regional'].choices = [('','Seleccione regional')] + list(self.fields['regional'].choices)[1:]
			self.fields ['regional'].label='Regional'
			self.fields ['regional'].widget.attrs['class']='form-control'
			self.fields ['estado'].label='Estado'
			self.fields ['estado'].widget.attrs['class']='form-control'

class SistemaForm(ModelForm):
	class Meta:
		model = SistemaOperativo
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(SistemaForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['sistema'].label='Sistema Operativo'
			self.fields ['sistema'].widget.attrs['class']= 'form-control'

class discoDuroForm(ModelForm):
	class Meta:
		model = DiscoDuro
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(discoDuroForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['disco'].label='Disco Duro'
			self.fields ['disco'].widget.attrs['class']= 'form-control'

class RAMForm(ModelForm):
	class Meta:
		model = RAM
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(RAMForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['ram'].label='Memoria RAM'
			self.fields ['ram'].widget.attrs['class']= 'form-control'

class ProcesadorForm(ModelForm):
	class Meta:
		model = Procesador
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(ProcesadorForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['procesador'].label='Procesador'
			self.fields ['procesador'].widget.attrs['class']= 'form-control'

class tipoEquipoForm(ModelForm):
	class Meta:
		model = TipoEquipo
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(tipoEquipoForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['tipo'].label='Tipo de Equipo'
			self.fields ['tipo'].widget.attrs['class']= 'form-control'

class MarcaForm(ModelForm):
	class Meta:
		model = Marca
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(MarcaForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['tipo'].label='Tipo de Equipo'
			self.fields ['tipo'].widget.attrs['class']= 'form-control'
			self.fields ['marca'].label='Marca'
			self.fields ['marca'].widget.attrs['class']= 'form-control'

class ModeloForm(ModelForm):
	class Meta:
		model = Modelo
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(ModeloForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['marca'].label='Marca de Equipo'
			self.fields ['marca'].widget.attrs['class']= 'form-control'
			self.fields ['modelo'].label='Modelo de Equipo'
			self.fields ['modelo'].widget.attrs['class']= 'form-control'

class MantenimientoForm(ModelForm):
	class Meta:
		model = Mantenimiento
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super (MantenimientoForm,self).__init__	(*args,**kwargs)
		for campo in self.fields:
			self.fields ['codigo_equipo'].choices = [('', 'Seleccione Equipo')] + list(self.fields['codigo_equipo'].choices)[1:]
			self.fields ['codigo_equipo'].label='Codigo Equipo'
			self.fields [campo].widget.attrs['class']='form-control'
			self.fields ['fecha_salida'].widget.attrs['size']=10
			self.fields ['fecha_salida'].label='Fecha de Salida'
			self.fields ['cod_empleado'].choices = [('','Seleccione empleado')] + list(self.fields['cod_empleado'].choices)[1:]
			self.fields ['cod_empleado'].label='Codigo Empleado'

class MantenimientoImpresorasForm(ModelForm):
	class Meta:
		model = OtroMantenimiento
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super (MantenimientoImpresorasForm,self).__init__	(*args,**kwargs)
		for campo in self.fields:
			self.fields ['codigo_Inventario'].choices = [('', 'Seleccione Equipo')] + list(self.fields['codigo_Inventario'].choices)[1:]
			self.fields ['codigo_Inventario'].label='Codigo del Equipo'
			self.fields [campo].widget.attrs['class']='form-control'
			self.fields ['fecha_salida'].widget.attrs['size']=10
			self.fields ['fecha_salida'].label='Fecha de Salida'
			self.fields ['proveedor'].choices = [('','Seleccione Proveedor')] + list(self.fields['proveedor'].choices)[1:]
			self.fields ['proveedor'].label='Proveedor'
			self.fields ['cod_empleado'].choices = [('','Seleccione empleado')] + list(self.fields['cod_empleado'].choices)[1:]
			self.fields ['cod_empleado'].label='Codigo Empleado'

class GarantiaForm(ModelForm):
	class Meta:
		model = Garantia
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super (GarantiaForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields [campo].widget.attrs['class']='form-control'
			self.fields ['codigo_equipo'].choices = [('', 'Seleccione Equipo')] + list(self.fields['codigo_equipo'].choices)[1:]
			self.fields ['codigo_equipo'].label='Codigo Equipo'
			self.fields ['Fecha_aperturaCaso'].widget.attrs['size']=10
			self.fields ['Fecha_aperturaCaso'].label='Fecha de Apertura de Caso'
			self.fields ['Fecha_entregaProducto'].widget.attrs['data-mask']='99/99/9999'
			self.fields ['Fecha_entregaProducto'].label='Fecha Entrega de Producto'
			self.fields ['cod_empleado'].choices=[('','Seleccione empleado')]	+ list(self.fields['cod_empleado'].choices)[1:]
			self.fields ['cod_empleado'].label='Codigo Empleado'

class AsignacionForm(ModelForm):
	class Meta:
		model = Asignacion
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(AsignacionForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['codigo_equipo'].choices= [('','Seleccione Equipo')] + list(self.fields['codigo_equipo'].choices)[1:]
			self.fields ['codigo_equipo'].label='Codigo Equipo'
			self.fields ['cod_empleadoRecibe'].choices=[('','Selecione empleado')]+ list	(self.fields['cod_empleadoRecibe'].choices)[1:]
			self.fields ['cod_empleadoRecibe'].label='Codigo de Empleado que Recibe'
			self.fields ['cod_empleadoEntrega'].choices=[('','Seleccione empleado')]+ list(self.fields['cod_empleadoEntrega'].choices)[1:]
			self.fields ['cod_empleadoEntrega'].label='Codigo de Empleado que Entrega'
			self.fields ['Comentario'].widget.attrs['class']='form-control'

class AsignacionImpresorasForm(ModelForm):
	class Meta:
		model = AsignacionImpresoras
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(AsignacionImpresorasForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields ['codigo_Inventario'].choices= [('','Seleccione Equipo')] + list(self.fields['codigo_Inventario'].choices)[1:]
			self.fields ['codigo_Inventario'].label='Codigo Equipo'
			self.fields ['cod_empleadoRecibe'].choices=[('','Selecione empleado')]+ list	(self.fields['cod_empleadoRecibe'].choices)[1:]
			self.fields ['cod_empleadoRecibe'].label='Codigo de Empleado que Recibe'
			self.fields ['cod_empleadoEntrega'].choices=[('','Seleccione empleado')]+ list(self.fields['cod_empleadoEntrega'].choices)[1:]
			self.fields ['cod_empleadoEntrega'].label='Codigo de Empleado que Entrega'
			self.fields ['Comentario'].widget.attrs['class']='form-control'
			self.fields ['estadoAsignacion'].label='Estado'
			self.fields ['estadoAsignacion'].widget.attrs['class']='form-control'

class ProveedorForm(ModelForm):
	class Meta:
		model = EmpresaProveedor
		fields= '__all__'
	def __init__(self, *args, **kwargs):
	    super(ProveedorForm, self).__init__(*args, **kwargs)
	    for campo in self.fields:
	    	self.fields	['RTN'].widget.attrs['class']='form-control	'
	    	self.fields ['RTN'].label='RTN de Proveedor'
	    	self.fields	['nombre'].widget.attrs['class']='form-control'
	    	self.fields ['nombre'].label='Nombre de la Empresa'
	    	self.fields	['correo'].widget.attrs['class']='form-control'
	    	self.fields ['correo'].label='Correo Electronico'

class TelefonoProveedorForm(ModelForm):
	class Meta:
		model = TelefonoProveedor
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(TelefonoProveedorForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields	['EmpresaProveedor'].choices=[('','Selecione Proveedor')]+ list(self.fields['EmpresaProveedor'].choices)[1:]
			self.fields ['EmpresaProveedor'].label='Nombre de la Empresa Proveedor'
			self.fields ['telefono'].label = 'Telefono'
			self.fields ['telefono'].widget.attrs['data-mask']='9999-9999'
			self.fields	[campo].widget.attrs['class']='form-control'

class DireccionProveedorForm(ModelForm):
	class Meta:
		model = DireccionProveedor
		fields= '__all__'
	def __init__(self,*args,**kwargs):
		super(DireccionProveedorForm,self).__init__(*args,**kwargs)
		for campo in self.fields:
			self.fields	['EmpresaProveedor'].choices=[('','Seleccione Proveedor')]+list(self.fields['EmpresaProveedor'].choices)[1:]
			self.fields ['EmpresaProveedor'].label='Nombre de la Empresa Proveedor'
			self.fields	['direccion'].label='Direccion'
			self.fields	['Comentario'].widget.attrs['class']='form-control'






