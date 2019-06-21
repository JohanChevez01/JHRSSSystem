
	
	$.ajax({
		type:'POST',
		url:'descargo/nuevo.html',
		data: {'peticion': 'cargar_Empleado'}
	})
	.done(function(lista_emp){
		$('#CodEquipo').html(lista_equ)
	})
	.fail(function(){
		alert('Hubo un error al cargar los empleados')
	})
