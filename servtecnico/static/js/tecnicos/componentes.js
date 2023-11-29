function toggleDropdown() {
    var dropdownMenu = document.getElementById("dropdownMenu");
    dropdownMenu.classList.toggle("show");
}

// Obtener el valor seleccionado del tipo
function obtenerTipoSeleccionado() {
    var radios = document.getElementsByName('tipo');
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            return radios[i].value;
        }
    }

    // Si no se ha seleccionado nada, devolver null o manejar según sea necesario
    return null;
}

// Alternativamente, si estás utilizando la lista desplegable (dropdown)
function obtenerTipoSeleccionadoDropdown() {
    var dropdown = document.getElementById('tipo');
    return dropdown.value;
}