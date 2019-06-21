from django.conf.urls import url
from . import views


# /Inventory/

app_name='Inventory'

urlpatterns =[

	url(r'^admin/$', views.admin, name='admin'),
	url(r'^recursosHumanos/$', views.recursosH, name='recursosH'),
	url(r'^compras/$', views.compras, name='compras'),
	url(r'^IT/$', views.IT, name='IT'),


#========================================================================================================================
#==================                URL ADMINISTRADOR DE SOFTWARE               ==========================================
#========================================================================================================================
	
	url(r'^usuario/$', views.usuario, name='usuario'),
	url(r'^usuario/(?P<id>\d+)/$', views.editarusuario, name='editarusuario'),
	url(r'^usuario/nuevo/$', views.nuevousuario, name='nuevousuario'),

	url(r'^empleado/$', views.empleado, name='empleado'),
	url(r'^empleado/(?P<id>\d+)/$', views.editarempleado, name='editarempleado'),
	url(r'^empleado/nuevo/$', views.nuevoempleado, name='nuevoempleado'),
	url(r'^equipo/empleado/(?P<id>\d+)/$', views.equipoempleado, name='equipoempleado'),
	url(r'^equipo/informacion/(?P<id>\d+)/$', views.InformacionEquipo, name='InformacionEquipo'),
	url(r'^equipo/empleado/entrega/(?P<id>\d+)/$', views.EquipoEmpleadoEntrega, name='EquipoEmpleadoEntrega'),
	
	url(r'^telefono/$', views.telefonoempleado, name='telefonoempleado'),
	url(r'^telefono/(?P<id>\d+)/$', views.editartelefonoempleado, name='editartelefonoempleado'),
	url(r'^telefono/nuevo/$', views.nuevotelefonoempleado, name='nuevotelefonoempleado'),
	url(r'^telefono/eliminar/(?P<id>\d+)/$', views.eliminartelefonoempleado, name='eliminartelefonoempleado'),

	url(r'^direccion/$', views.direccionempleado, name='direccionempleado'),
	url(r'^direccion/(?P<id>\d+)/$', views.editardireccionempleado, name='editardireccionempleado'),
	url(r'^direccion/nuevo/$', views.nuevodireccionempleado, name='nuevodireccionempleado'),
	url(r'^direccion/eliminar/(?P<id>\d+)/$', views.eliminardireccionempleado, name='eliminardireccionempleado'),

	url(r'^contrato/$', views.contrato, name='contrato'),
	url(r'^contrato/(?P<id>\d+)/$', views.editarcontrato, name='editarcontrato'),
	url(r'^contrato/nuevo/$', views.nuevocontrato, name='nuevocontrato'),

	url(r'^salario/$', views.salario, name='salario'),
	url(r'^salario/(?P<id>\d+)/$', views.editarsalario, name='editarsalario'),
	url(r'^salario/nuevo/$', views.nuevosalario, name='nuevosalario'),

	url(r'^profesion/$', views.profesion, name='profesion'),
	url(r'^profesion/(?P<id>\d+)/$', views.editarprofesion, name='editarprofesion'),
	url(r'^profesion/nuevo/$', views.nuevoprofesion, name='nuevoprofesion'),

	url(r'^cargo/$', views.cargo, name='cargo'),
	url(r'^cargo/(?P<id>\d+)/$', views.editarcargo, name='editarcargo'),
	url(r'^cargo/nuevo/$', views.nuevocargo, name='nuevocargo'),

	url(r'^departamento/$', views.departamento, name='departamento'),
	url(r'^departamento/(?P<id>\d+)/$', views.editardepartamento, name='editardepartamento'),
	url(r'^departamento/nuevo/$', views.nuevodepartamento, name='nuevodepartamento'),

	url(r'^regional/$', views.regional, name='regional'),
	url(r'^regional/(?P<id>\d+)/$', views.editarregional, name='editarregional'),
	url(r'^regional/nuevo/$', views.nuevoregional, name='nuevoregional'),

	url(r'^equipo/$', views.equipo, name='equipo'),
	url(r'^equipo/(?P<id>\d+)/$', views.editarequipo, name='editarequipo'),
	url(r'^equipo/nuevo/$', views.nuevoequipo, name='nuevoequipo'),
	url(r'^equipo/historial/(?P<id>\d+)$', views.historialequipo, name='historialequipo'),
	url(r'^equipo/marca/$', views.marca_json, name='marca_json'),
	url(r'^equipo/marca/modelo/$', views.modelo_json, name='modelo_json'),

	url(r'^impresoras/$', views.impresoras, name='impresoras'),
	url(r'^impresoras/(?P<id>\d+)/$', views.editarimpresoras, name='editarimpresoras'),
	url(r'^impresoras/nuevo/$', views.nuevoimpresoras, name='nuevoimpresoras'),
	url(r'^impresoras/historial/(?P<id>\d+)$', views.historialimpresoras, name='historialimpresoras'),
	url(r'^impresoras/marca/$', views.marcai_json, name='marcai_json'),
	url(r'^impresoras/marca/modelo/$', views.modeloi_json, name='modeloi_json'),

	url(r'^asignacion/$', views.asignacion, name='asignacion'),
	url(r'^asignacion/(?P<id>\d+)/$', views.editarasignacion, name='editarasignacion'),
	url(r'^asignacion/nuevo/$', views.nuevoasignacion, name='nuevoasignacion'),

	url(r'^asignacionImpresoras/$', views.asignacionImpresoras, name='asignacionImpresoras'),
	url(r'^asignacionImpresoras/(?P<id>\d+)/$', views.editarasignacionImpresoras, name='editarasignacionImpresoras'),
	url(r'^asignacionImpresoras/nuevo/$', views.nuevoasignacionImpresoras, name='nuevoasignacionImpresoras'),

	url(r'^descargo/$', views.descargo, name='descargo'),
	url(r'^descargo/nuevo/$', views.nuevodescargo, name='nuevodescargo'),
	url(r'^descargo/busqueda/(?P<pk>\d+)/$', views.Entregadescargo, name='Edescargo'),
	url(r'^descargo/emp/(?P<pk>\d+)/$', views.EmpleadoEntrega, name='EEntrega'),

	url(r'^descargoImpresoras/$', views.descargoImpresoras, name='descargoImpresoras'),
	url(r'^descargoImpresoras/nuevo/$', views.nuevodescargoImpresoras, name='nuevodescargoImpresoras'),
	url(r'^descargoImpresoras/busqueda/(?P<pk>\d+)/$', views.EntregadescargoImpresoras, name='EdescargoImpresoras'),
	url(r'^descargoImpresoras/emp/(?P<pk>\d+)/$', views.EmpleadoEntregaImpresoras, name='EEntregaImpresoras'),

	url(r'^mantenimiento/$', views.mantenimiento, name='mantenimiento'),
	url(r'^mantenimiento/(?P<id>\d+)/$', views.editarmantenimiento, name='editarmantenimiento'),
	url(r'^mantenimiento/nuevo/$', views.nuevomantenimiento, name='nuevomantenimiento'),

	url(r'^mantenimientoImpresora/$', views.mantenimientoImpresora, name='mantenimientoImpresora'),
	url(r'^mantenimientoImpresora/(?P<id>\d+)/$', views.editarmantenimientoImpresora, name='editarmantenimientoImpresora'),
	url(r'^mantenimientoImpresora/nuevo/$', views.nuevomantenimientoImpresora, name='nuevomantenimientoImpresora'),

	url(r'^garantia/$', views.garantia, name='garantia'),
	url(r'^garantia/(?P<id>\d+)/$', views.editargarantia, name='editargarantia'),
	url(r'^garantia/nuevo/$', views.nuevogarantia, name='nuevogarantia'),

	url(r'^tipoEquipo/$', views.tipoEquipo, name='tipoEquipo'),
	url(r'^tipoEquipo/(?P<id>\d+)/$', views.editartipoEquipo, name='editartipoEquipo'),
	url(r'^tipoEquipo/nuevo/$', views.nuevotipoEquipo, name='nuevotipoEquipo'),

	url(r'^marca/$', views.marca, name='marca'),
	url(r'^marca/(?P<id>\d+)/$', views.editarmarca, name='editarmarca'),
	url(r'^marca/nuevo/$', views.nuevomarca, name='nuevomarca'),

	url(r'^modelo/$', views.modelo, name='modelo'),
	url(r'^modelo/(?P<id>\d+)/$', views.editarmodelo, name='editarmodelo'),
	url(r'^modelo/nuevo/$', views.nuevomodelo, name='nuevomodelo'),

	url(r'^sistema/$', views.sistema, name='sistema'),
	url(r'^sistema/(?P<id>\d+)/$', views.editarsistema, name='editarsistema'),
	url(r'^sistema/nuevo/$', views.nuevosistema, name='nuevosistema'),

	url(r'^discoDuro/$', views.discoDuro, name='discoDuro'),
	url(r'^discoDuro/(?P<id>\d+)/$', views.editardiscoDuro, name='editardiscoDuro'),
	url(r'^discoDuro/nuevo/$', views.nuevodiscoDuro, name='nuevodiscoDuro'),

	url(r'^memoriaRAM/$', views.memoriaRAM, name='memoriaRAM'),
	url(r'^memoriaRAM/(?P<id>\d+)/$', views.editarmemoriaRAM, name='editarmemoriaRAM'),
	url(r'^memoriaRAM/nuevo/$', views.nuevomemoriaRAM, name='nuevomemoriaRAM'),

	url(r'^procesador/$', views.procesador, name='procesador'),
	url(r'^procesador/(?P<id>\d+)/$', views.editarprocesador, name='editarprocesador'),
	url(r'^procesador/nuevo/$', views.nuevoprocesador, name='nuevoprocesador'),

	url(r'^proveedor/$', views.proveedor, name='proveedor'),
	url(r'^proveedor/(?P<id>\d+)/$', views.editarproveedor, name='editarproveedor'),
	url(r'^proveedor/nuevo/$', views.nuevoproveedor, name='nuevoproveedor'),

	url(r'^direccion_proveedor/$', views.direccionproveedor, name='direccionproveedor'),
	url(r'^direccion_proveedor/(?P<id>\d+)/$', views.editardireccionproveedor, name='editardireccionproveedor'),
	url(r'^direccion_proveedor/nuevo/$', views.nuevodireccionproveedor, name='nuevodireccionproveedor'),
	url(r'^direccion_proveedor/eliminar/(?P<id>\d+)/$', views.eliminardireccionproveedor, name='eliminardireccionproveedor'),

	url(r'^telefono_proveedor/$', views.telefonoproveedor, name='telefonoproveedor'),
	url(r'^telefono_proveedor/(?P<id>\d+)/$', views.editartelefonoproveedor, name='editartelefonoproveedor'),
	url(r'^telefono_proveedor/nuevo/$', views.nuevotelefonoproveedor, name='nuevotelefonoproveedor'),
	url(r'^telefono_proveedor/eliminar/(?P<id>\d+)/$', views.eliminartelefonoproveedor, name='eliminartelefonoproveedor'),

#========================================================================================================================
#==================                URL RECURSOS HUMANOS               ===================================================
#========================================================================================================================

	url(r'^usuarioR/$', views.usuarioR, name='usuarioR'),
	url(r'^usuarioR/(?P<id>\d+)/$', views.editarusuarioR, name='editarusuarioR'),
	url(r'^usuarioR/nuevo/$', views.nuevousuarioR, name='nuevousuarioR'),

	url(r'^empleadoR/$', views.empleadoR, name='empleadoR'),
	url(r'^empleadoR/(?P<id>\d+)/$', views.editarempleadoR, name='editarempleadoR'),
	url(r'^empleadoR/nuevo/$', views.nuevoempleadoR, name='nuevoempleadoR'),

	url(r'^telefonoR/$', views.telefonoempleadoR, name='telefonoempleadoR'),
	url(r'^telefonoR/(?P<id>\d+)/$', views.editartelefonoempleadoR, name='editartelefonoempleadoR'),
	url(r'^telefonoR/nuevo/$', views.nuevotelefonoempleadoR, name='nuevotelefonoempleadoR'),
	url(r'^telefono/eliminar/(?P<id>\d+)/$', views.eliminartelefonoempleadoR, name='eliminartelefonoempleadoR'),

	url(r'^direccionR/$', views.direccionempleadoR, name='direccionempleadoR'),
	url(r'^direccionR/(?P<id>\d+)/$', views.editardireccionempleadoR, name='editardireccionempleadoR'),
	url(r'^direccionR/nuevo/$', views.nuevodireccionempleadoR, name='nuevodireccionempleadoR'),
	url(r'^direccion/eliminar/(?P<id>\d+)/$', views.eliminardireccionempleadoR, name='eliminardireccionempleado'),

	url(r'^contratoR/$', views.contratoR, name='contratoR'),
	url(r'^contratoR/(?P<id>\d+)/$', views.editarcontratoR, name='editarcontratoR'),
	url(r'^contratoR/nuevo/$', views.nuevocontratoR, name='nuevocontratoR'),

	url(r'^salarioR/$', views.salarioR, name='salarioR'),
	url(r'^salarioR/(?P<id>\d+)/$', views.editarsalarioR, name='editarsalarioR'),
	url(r'^salarioR/nuevo/$', views.nuevosalarioR, name='nuevosalarioR'),

	url(r'^profesionR/$', views.profesionR, name='profesionR'),
	url(r'^profesionR/(?P<id>\d+)/$', views.editarprofesionR, name='editarprofesionR'),
	url(r'^profesionR/nuevo/$', views.nuevoprofesionR, name='nuevoprofesionR'),

	url(r'^cargoR/$', views.cargoR, name='cargoR'),
	url(r'^cargoR/(?P<id>\d+)/$', views.editarcargoR, name='editarcargoR'),
	url(r'^cargoR/nuevo/$', views.nuevocargoR, name='nuevocargoR'),

	url(r'^departamentoR/$', views.departamentoR, name='departamentoR'),
	url(r'^departamentoR/(?P<id>\d+)/$', views.editardepartamentoR, name='editardepartamentoR'),
	url(r'^departamentoR/nuevo/$', views.nuevodepartamentoR, name='nuevodepartamentoR'),

	url(r'^regionalR/$', views.regionalR, name='regionalR'),
	url(r'^regionalR/(?P<id>\d+)/$', views.editarregionalR, name='editarregionalR'),
	url(r'^regionalR/nuevo/$', views.nuevoregionalR, name='nuevoregionalR'),

#========================================================================================================================
#===========================                URL COMPRAS               ===================================================
#========================================================================================================================
	url(r'^proveedorC/$', views.proveedorC, name='proveedorC'),
	url(r'^proveedorC/(?P<id>\d+)/$', views.editarproveedorC, name='editarproveedorC'),
	url(r'^proveedorC/nuevo/$', views.nuevoproveedorC, name='nuevoproveedorC'),

	url(r'^telefono_proveedorC/$', views.telefonoproveedorC, name='telefonoproveedorC'),
	url(r'^telefono_proveedorC/(?P<id>\d+)/$', views.editartelefonoproveedorC, name='editartelefonoproveedorC'),
	url(r'^telefono_proveedorC/nuevo/$', views.nuevotelefonoproveedorC, name='nuevotelefonoproveedorC'),
	url(r'^telefono_proveedor/eliminar/(?P<id>\d+)/$', views.eliminartelefonoproveedorC, name='eliminartelefonoproveedorC'),

	url(r'^direccion_proveedorC/$', views.direccionproveedorC, name='direccionproveedorC'),
	url(r'^direccion_proveedorC/(?P<id>\d+)/$', views.editardireccionproveedorC, name='editardireccionproveedorC'),
	url(r'^direccion_proveedorC/nuevo/$', views.nuevodireccionproveedorC, name='nuevodireccionproveedorC'),
	url(r'^direccion_proveedor/eliminar/(?P<id>\d+)/$', views.eliminardireccionproveedorC, name='eliminardireccionproveedorC'),

#========================================================================================================================
#===========================                URL INFORMATICA & TECNOLOGIA               ==================================
#========================================================================================================================
	url(r'^equipos/$', views.equipos, name='equipos'),
	url(r'^mantenimientosdeequipo/$', views.mantenimientosdeequipo, name='mantenimientosdeequipo'),
	url(r'^herramientasIT/$', views.herramientasIT, name='herramientasIT'),
	url(r'^asignaciones/$', views.asignaciones, name='asignaciones'),
	url(r'^descargos/$', views.descargos, name='descargos'),

	url(r'^equipoIT/$', views.equipoIT, name='equipoIT'),
	url(r'^equipoIT/(?P<id>\d+)/$', views.editarequipoIT, name='editarequipoIT'),
	url(r'^equipoIT/nuevo/$', views.nuevoequipoIT, name='nuevoequipoIT'),

	url(r'^impresorasIT/$', views.impresorasIT, name='impresorasIT'),
	url(r'^impresorasIT/(?P<id>\d+)/$', views.editarimpresorasIT, name='editarimpresorasIT'),
	url(r'^impresorasIT/nuevo/$', views.nuevoimpresorasIT, name='nuevoimpresorasIT'),

	url(r'^asignacionIT/$', views.asignacionIT, name='asignacionIT'),
	url(r'^asignacionIT/(?P<id>\d+)/$', views.editarasignacionIT, name='editarasignacionIT'),
	url(r'^asignacionIT/nuevo/$', views.nuevoasignacionIT, name='nuevoasignacionIT'),

	url(r'^descargoIT/$', views.descargoIT, name='descargoIT'),
	url(r'^descargoIT/nuevo/$', views.nuevodescargoIT, name='nuevodescargoIT'),
	url(r'^descargoIT/busqueda/(?P<pk>\d+)/$', views.EntregadescargoIT, name='EdescargoIT'),
	url(r'^descargoIT/emp/(?P<pk>\d+)/$', views.EmpleadoEntregaIT, name='EEntregaIT'),

	url(r'^asignacionImpresorasIT/$', views.asignacionImpresorasIT, name='asignacionImpresorasIT'),
	url(r'^asignacionImpresorasIT/(?P<id>\d+)/$', views.editarasignacionImpresorasIT, name='editarasignacionImpresorasIT'),
	url(r'^asignacionImpresorasIT/nuevo/$', views.nuevoasignacionImpresorasIT, name='nuevoasignacionImpresorasIT'),
	
	url(r'^descargoImpresorasIT/$', views.descargoImpresorasIT, name='descargoImpresorasIT'),
	url(r'^descargoImpresorasIT/nuevo/$', views.nuevodescargoImpresorasIT, name='nuevodescargoImpresorasIT'),
	url(r'^descargoImpresorasIT/busqueda/(?P<pk>\d+)/$', views.EntregadescargoImpresorasIT, name='EdescargoImpresorasIT'),
	url(r'^descargoImpresorasIT/emp/(?P<pk>\d+)/$', views.EmpleadoEntregaImpresorasIT, name='EEntregaImpresorasIT'),
	
	url(r'^mantenimientoIT/$', views.mantenimientoIT, name='mantenimientoIT'),
	url(r'^mantenimientoIT/(?P<id>\d+)/$', views.editarmantenimientoIT, name='editarmantenimientoIT'),
	url(r'^mantenimientoIT/nuevo/$', views.nuevomantenimientoIT, name='nuevomantenimientoIT'),

	url(r'^mantenimientoImpresoraIT/$', views.mantenimientoImpresoraIT, name='mantenimientoImpresoraIT'),
	url(r'^mantenimientoImpresoraIT/(?P<id>\d+)/$', views.editarmantenimientoImpresoraIT, name='editarmantenimientoImpresoraIT'),
	url(r'^mantenimientoImpresoraIT/nuevo/$', views.nuevomantenimientoImpresoraIT, name='nuevomantenimientoImpresoraIT'),

	url(r'^garantiaIT/$', views.garantiaIT, name='garantiaIT'),
	url(r'^garantiaIT/(?P<id>\d+)/$', views.editargarantiaIT, name='editargarantiaIT'),
	url(r'^garantiaIT/nuevo/$', views.nuevogarantiaIT, name='nuevogarantiaIT'),

	url(r'^tipoEquipoIT/$', views.tipoEquipoIT, name='tipoEquipoIT'),
	url(r'^tipoEquipoIT/(?P<id>\d+)/$', views.editartipoEquipoIT, name='editartipoEquipoIT'),
	url(r'^tipoEquipoIT/nuevo/$', views.nuevotipoEquipoIT, name='nuevotipoEquipoIT'),

	url(r'^marcaIT/$', views.marcaIT, name='marcaIT'),
	url(r'^marcaIT/(?P<id>\d+)/$', views.editarmarcaIT, name='editarmarcaIT'),
	url(r'^marcaIT/nuevo/$', views.nuevomarcaIT, name='nuevomarcaIT'),

	url(r'^modeloIT/$', views.modeloIT, name='modeloIT'),
	url(r'^modeloIT/(?P<id>\d+)/$', views.editarmodeloIT, name='editarmodeloIT'),
	url(r'^modeloIT/nuevo/$', views.nuevomodeloIT, name='nuevomodeloIT'),

	url(r'^sistemaIT/$', views.sistemaIT, name='sistemaIT'),
	url(r'^sistemaIT/(?P<id>\d+)/$', views.editarsistemaIT, name='editarsistemaIT'),
	url(r'^sistemaIT/nuevo/$', views.nuevosistemaIT, name='nuevosistemaIT'),

	url(r'^discoDuroIT/$', views.discoDuroIT, name='discoDuroIT'),
	url(r'^discoDuroIT/(?P<id>\d+)/$', views.editardiscoDuroIT, name='editardiscoDuroIT'),
	url(r'^discoDuroIT/nuevo/$', views.nuevodiscoDuroIT, name='nuevodiscoDuroIT'),

	url(r'^memoriaRAMIT/$', views.memoriaRAMIT, name='memoriaRAMIT'),
	url(r'^memoriaRAMIT/(?P<id>\d+)/$', views.editarmemoriaRAMIT, name='editarmemoriaRAMIT'),
	url(r'^memoriaRAMIT/nuevo/$', views.nuevomemoriaRAMIT, name='nuevomemoriaRAMIT'),

	url(r'^procesadorIT/$', views.procesadorIT, name='procesadorIT'),
	url(r'^procesadorIT/(?P<id>\d+)/$', views.editarprocesadorIT, name='editarprocesadorIT'),
	url(r'^procesadorIT/nuevo/$', views.nuevoprocesadorIT, name='nuevoprocesadorIT'),

#========================================================================================================================
#===========================                        URL REPORTES                       ==================================
#========================================================================================================================
	# url(r'^empleadopdf/$', EmpleadoPdfView.as_view(), name = 'empleadopdf'),
    url(r'^empleadospdf/$', views.empleadopdf, name = 'empleadopdf'),
    url(r'^inforempleadopdf/(?P<id>\d+)/$', views.inforempleadopdf, name = 'inforempleadopdf'),
    url(r'^empleado/asignaciones/(?P<id>\d+)/$', views.empleadoAsignacion, name = 'empleadoAsignacion'),

    url(r'^equipopdf/$', views.equipopdf, name = 'equipopdf'),
    url(r'^impresoraspdf/$', views.impresoraspdf, name = 'impresoraspdf'),
    url(r'^asignacionpdf/$', views.asignacionpdf, name = 'asignacionpdf'),
    url(r'^proveedorpdf/$', views.proveedorpdf, name = 'proveedorpdf'),
    
    url(r'^mantenimientopdf/$', views.mantenimientopdf, name = 'mantenimientopdf'),
    url(r'^otrosmantenimientopdf/$', views.otrosmantenimientopdf, name = 'otrosmantenimientopdf'),

	url(r'^reportesGenerales/$', views.reportesGenerales, name='reportesGenerales'),
	url(r'^reportesAsignacion/$', views.reportesAsignacion, name='reportesAsignacion'),
]