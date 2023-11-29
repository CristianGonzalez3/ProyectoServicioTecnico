function volver() {
    window.location.href = '{% url "pagina_principal_tecnico" %}';
}

function enviarDatos() {
    // Lógica para enviar datos o realizar otras acciones
    alert('Datos enviados o acción realizada.');
}

function redirigirAgregar() {
    window.location.href = 'agregar.html';
}

function generarNuevoId(datos) {
    var maxId = 0;
    datos.forEach(function (dato) {
        if (dato.id > maxId) {
            maxId = dato.id;
        }
    });
    return maxId + 1;
}
