let id = 1; // Variable para asignar ID único a cada cuadro

        function agregarCuadro() {
            const container = document.getElementById('container');

            const cuadro = document.createElement('div');
            cuadro.classList.add('item');

            cuadro.innerHTML = `
                <label>ID:</label>
                <input type="text" id="id${id}" value="${id}" disabled>
                <label>Nombre:</label>
                <input type="text" id="nombre${id}" placeholder="Nombre">
                <label>Descripción:</label>
                <input type="text" id="descripcion${id}" placeholder="Descripción">
                <label>Stock:</label>
                <input type="text" id="stock${id}" placeholder="Stock">
            `;

            container.appendChild(cuadro);
            guardarEnLocalStorage(id);
            id++;
        }

        function eliminarCuadro() {
            const idEliminar = document.getElementById('inputEliminar').value;
            const cuadroAEliminar = document.getElementById(`id${idEliminar}`);

            if (cuadroAEliminar) {
                cuadroAEliminar.parentNode.remove();
                localStorage.removeItem(`id${idEliminar}`);
            }
        }

        function guardarEnLocalStorage(id) {
            // Guardar datos en localStorage
            const nombre = document.getElementById(`nombre${id}`).value || '';
            const descripcion = document.getElementById(`descripcion${id}`).value || '';
            const stock = document.getElementById(`stock${id}`).value || '';

            localStorage.setItem(`id${id}`, JSON.stringify({ nombre, descripcion, stock }));
        }

        window.onload = function () {
    id = 1; // Establecer id en 1

    for (let i = 1; i <= localStorage.length; i++) {
        const datos = JSON.parse(localStorage.getItem(`id${i}`));

        if (datos) {
            const container = document.getElementById('container');

            const cuadro = document.createElement('div');
            cuadro.classList.add('item');

            cuadro.innerHTML = `
                <label>ID:</label>
                <input type="text" id="id${id}" value="${id}" disabled>
                <label>Nombre:</label>
                <input type="text" id="nombre${id}" value="${datos.nombre}" placeholder="Nombre">
                <label>Descripción:</label>
                <input type="text" id="descripcion${id}" value="${datos.descripcion}" placeholder="Descripción">
                <label>Stock:</label>
                <input type="text" id="stock${id}" value="${datos.stock}" placeholder="Stock">
            `;

            container.appendChild(cuadro);
            id++; // Incrementar id para evitar conflictos
        }
    }
};
