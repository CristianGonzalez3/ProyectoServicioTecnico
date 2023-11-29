      // La función para redirigir debería estar fuera del evento submit
      function volver() {
        window.location.href = 'Reparacioness.html';
    }

    // Evento submit del formulario
    document.getElementById('miFormulario').addEventListener('submit', function (event) {
        event.preventDefault(); // Evitar el envío por defecto del formulario
        guardarYRedirigir();
    });

    // Función para guardar y redirigir
    function guardarYRedirigir() {
        // Obtener datos del formulario utilizando identificadores únicos
        var nombreEquipo = document.getElementById('equipo').value;
        var reporte = document.getElementById('reporte').value;
        var fechaReporte = document.getElementById('fechaReporte').value;
        var fechaReparacion = document.getElementById('fechaReparacion').value;
        var descripcionReparacion = document.getElementById('descripcionReparacion').value;

        // Obtener datos guardados o inicializar un array vacío
        var datosGuardados = JSON.parse(localStorage.getItem('datosReparaciones')) || [];

        // Crear un objeto con los datos y asignar un ID simple
        var nuevoDato = {
            id: datosGuardados.length + 1,
            nombreEquipo: nombreEquipo,
            reporte: reporte,
            fechaReporte: fechaReporte,
            fechaReparacion: fechaReparacion,
            descripcionReparacion: descripcionReparacion
        };

        // Agregar el nuevo dato a la lista
        datosGuardados.push(nuevoDato);

        // Guardar la lista actualizada en localStorage
        localStorage.setItem('datosReparaciones', JSON.stringify(datosGuardados));

        // Redirigir a la página de Reparaciones con los datos actualizados
        window.location.href = 'Reparacioness.html';
    }