$(function(){

	$('.btn-follow').on('click', function(){
		var id = $(this).attr('data-id');
		var url= $(this).attr('data-url');

		$.get(url, {'id': id}, function(data) {
			console.log('Respuesta del Servidor:' + data.id);
		},'json');
	});

});