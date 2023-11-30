function mostrarSeguimiento() {
    document.getElementById("contenido").innerHTML = "<h1>Sección de Seguimiento</h1><p>Contenido de seguimiento.</p>";
}

function mostrarSolicitud() {
    document.getElementById("contenido").innerHTML = "<h1>Sección de Solicitud</h1><p>Contenido de solicitud.</p>";
}

function mostrarInforme() {
    document.getElementById("contenido").innerHTML = "<h1>Sección de Informe</h1><p>Contenido de informe.</p>";
}
function mostrarSolicitud(){
    window.location.href = 'solicitudd.html';
}
function mostrarSeguimiento() {
    window.location.href = 'seguimiento.html';
}
function mostrarInforme() {
    window.location.href = 'informe.html';
};