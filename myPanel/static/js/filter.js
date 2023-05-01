    // Obtener el elemento input donde se ingresa el término de búsqueda
    var input = document.getElementById("search");

    // Agregar un evento de cambio al input para ejecutar la función de filtrado
    input.addEventListener("input", filterTable);

    // Definir la función de filtrado
    function filterTable() {
        // Obtener el valor del input en mayúsculas
        var filter = input.value.toUpperCase();
        // Obtener el elemento tbody donde están las filas de datos
        var tbody = document.getElementById("table-body");
        // Obtener todas las filas del tbody
        var tr = tbody.getElementsByTagName("tr");
        // Iterar por cada fila
        for (var i = 0; i < tr.length; i++) {
            // Obtener todas las celdas de la fila
            var td = tr[i].getElementsByTagName("td");
            // Inicializar una variable para indicar si la fila debe mostrarse o no
            var show = false;
            // Iterar por cada celda
            for (var j = 0; j < td.length; j++) {
                // Obtener el contenido de la celda en mayúsculas
                var cell = td[j].innerHTML.toUpperCase();
                // Si el contenido de la celda contiene el valor del filtro
                if (cell.indexOf(filter) > -1) {
                    // Marcar la fila como que debe mostrarse
                    show = true;
                }
            }
            // Si la fila debe mostrarse
            if (show) {
                // Establecer el estilo display como vacío para que sea visible
                tr[i].style.display = "";
            } else {
                // Establecer el estilo

                tr[i].style.display = "none";
            }
        }
    }