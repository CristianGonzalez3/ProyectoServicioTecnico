

    // Función para volver a la página anterior
    function volver() {
        // Cambia 'nombre-del-archivo.html' con el nombre del HTML al que deseas redirigir
        window.location.href = 'Practica.html';
    }
    function redirigirAgregar() {
        // Cambia 'nombre-del-archivo-agregar.html' con el nombre del HTML de agregar
        window.location.href = 'agregar equipo.html';
    }
        // Función para agregar datos a la tabla en Equipos.html
    function agregarDatosEnTabla(datos) {
        // Obtener la referencia de la tabla
        var tabla = document.getElementById('miTabla');

        // Obtener la cantidad de filas presentes en la tabla
        var rowCount = tabla.rows.length;

        // Agregar una nueva fila al final de la tabla
        var row = tabla.insertRow(rowCount);

        // Insertar celdas en la nueva fila
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);

        // Agregar datos a las celdas
        cell1.innerHTML = rowCount;
        cell2.innerHTML = datos.nombre;
        cell3.innerHTML = datos.descripcion;
        cell4.innerHTML = datos.fecha;
    }
