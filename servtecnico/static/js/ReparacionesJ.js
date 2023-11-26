function volver() {
    window.location.href = 'Tecnico.html';
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

document.addEventListener("DOMContentLoaded", function () {
    var datosGuardados = JSON.parse(localStorage.getItem('datosReparaciones')) || [];
    var tbody = document.querySelector('.table tbody');

    // Eliminar las primeras 4 filas
    for (var i = 0; i < 4; i++) {
        tbody.deleteRow(0);
    }

    // Verificar y asignar IDs únicos
    datosGuardados.forEach(function (dato) {
        if (!dato.id) {
            dato.id = generarNuevoId(datosGuardados);
        }
    });

    // Actualizar la lista en localStorage con los nuevos IDs
    localStorage.setItem('datosReparaciones', JSON.stringify(datosGuardados));

    // Llenar la tabla con los datos
    datosGuardados.forEach(function (dato) {
        var row = tbody.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        var cell6 = row.insertCell(5);
        var cellCheckbox = row.insertCell(6); // Nueva celda para el checkbox

        cell1.textContent = dato.id;
        cell2.textContent = dato.nombreEquipo;
        cell3.textContent = dato.reporte;
        cell4.textContent = dato.fechaReporte;
        cell5.textContent = dato.fechaReparacion;
        cell6.textContent = dato.descripcionReparacion;

        // Añadir el checkbox a la nueva celda
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'seleccionar-checkbox';
        checkbox.setAttribute('aria-label', 'Checkbox for following text input');
        cellCheckbox.appendChild(checkbox);
    });
});

var btnAgregar = document.querySelector('.btn-success');

var btnAgregar = document.querySelector('.btn-success');

btnAgregar.addEventListener('click', function () {
    // Calcular el próximo ID
    var proximoId = generarNuevoId(datosGuardados);

    // Obtener datos del formulario utilizando identificadores únicos
    var nombreEquipo = document.getElementById('nombreEquipo').value;
    var reporte = document.getElementById('reporte').value;
    var fechaReporte = document.getElementById('fechaReporte').value;
    var fechaReparacion = document.getElementById('fechaReparacion').value;
    var descripcionReparacion = document.getElementById('descripcionReparacion').value;

    // Crear un objeto con los datos y el nuevo ID
    var nuevoDato = {
        id: proximoId,
        nombreEquipo: nombreEquipo,
        reporte: reporte,
        fechaReporte: fechaReporte,
        fechaReparacion: fechaReparacion,
        descripcionReparacion: descripcionReparacion
    };

    // Agregar el nuevo dato a la lista
    datosGuardados.push(nuevoDato);

    // Limpiar el cuerpo de la tabla
    tbody.innerHTML = "";

    // Llenar la tabla con los datos actualizados
    datosGuardados.forEach(function (dato) {
        var row = tbody.insertRow(-1);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        var cell6 = row.insertCell(5);
        var cellCheckbox = row.insertCell(6); // Nueva celda para el checkbox

        cell1.textContent = dato.id;
        cell2.textContent = dato.nombreEquipo;
        cell3.textContent = dato.reporte;
        cell4.textContent = dato.fechaReporte;
        cell5.textContent = dato.fechaReparacion;
        cell6.textContent = dato.descripcionReparacion;

        // Añadir el checkbox a la nueva celda
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.className = 'seleccionar-checkbox';
        checkbox.setAttribute('aria-label', 'Checkbox for following text input');
        cellCheckbox.appendChild(checkbox);
    });

    // Guardar la lista actualizada en localStorage
    localStorage.setItem('datosReparaciones', JSON.stringify(datosGuardados));
});