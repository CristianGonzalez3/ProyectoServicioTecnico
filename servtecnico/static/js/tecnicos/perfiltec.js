function agregarCampo(campo) {
    var nuevoCampo = prompt('Ingrese nuevo ' + campo + ':');
    if (nuevoCampo !== null && nuevoCampo !== '') {
        document.getElementById(campo).value = nuevoCampo;
    }
}

function guardarContacto() {
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var telefono = document.getElementById('telefono').value;
    var correo = document.getElementById('correo electronico').value;

    console.log('Nombre: ' + nombre);
    console.log('Apellido: ' + apellido);
    console.log('Teléfono: ' + telefono);
    console.log('Correo electronico: ' + correo );

    document.getElementById('formulario').reset();
}

function volver() {
    alert('Implementa la lógica para volver a la página anterior.');
}

document.getElementById('profilePicture').addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            document.getElementById('preview').src = e.target.result;
            document.getElementById('preview').style.display = 'block';
        };

        reader.readAsDataURL(file);
    }
});