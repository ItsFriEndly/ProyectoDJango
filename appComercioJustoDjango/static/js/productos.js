"use strict";

const buscador = document.getElementById("buscador");
const tabla = document.getElementById("tabla-productos");
const info = document.getElementById("buscador-info");

function crearCeldaEnlace(url, texto) {
    const celda = document.createElement("td");
    const enlace = document.createElement("a");
    enlace.href = url;
    enlace.textContent = texto;
    celda.append(enlace);
    return celda;
}

function pintarProductos(productos) {
    tabla.innerHTML = "";

    if (productos.length === 0) {
        const fila = document.createElement("tr");
        const celda = document.createElement("td");
        celda.colSpan = 4;
        celda.textContent = "No se ha encontrado ningún producto.";
        fila.append(celda);
        tabla.append(fila);
    }

    for (let producto of productos) {
        const fila = document.createElement("tr");
        const precio = document.createElement("td");
        precio.textContent = producto.precio + " €";

        fila.append(
            crearCeldaEnlace(producto.url, producto.nombre),
            crearCeldaEnlace(producto.url_categoria, producto.categoria),
            precio,
            crearCeldaEnlace(producto.url, "Ver detalle")
        );
        tabla.append(fila);
    }

    info.textContent = productos.length + " producto(s) encontrado(s)";
}

function buscarProductos() {
    const texto = buscador.value.trim();
    const url = buscador.dataset.url + "?q=" + encodeURIComponent(texto);

    fetch(url)
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                return Promise.reject("Error en la respuesta del servidor");
            }
        })
        .then(datos => pintarProductos(datos.productos))
        .catch(error => {
            info.textContent = "No se han podido cargar los productos.";
            console.log("Error: ", error);
        });
}

buscador.addEventListener("keyup", buscarProductos);
