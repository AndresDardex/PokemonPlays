$(document).ready(function() {
  // Escuchamos el evento submit del formulario
  $('form').submit(function(event) {
      // Detenemos el envío del formulario
      event.preventDefault();
      
      // Obtenemos el valor del input
      var pokemonBuscado = $('#pokemon-buscado').val();
      
      // Realizamos una petición AJAX para verificar si el pokemon existe
      $.ajax({
          url: '/buscar/',
          type: 'GET',
          data: { 'pokemon_buscado': pokemonBuscado },
          success: function(response) {
              // Si el pokemon existe, enviamos el formulario
              $('form').unbind('submit').submit();
          },
          error: function(xhr, status, error) {
              // Si hay un error, mostramos una alerta
              alert('El Pokémon no existe en la base de datos.');
          }
      });
  });
});


