"use strict";

const formulario = document.getElementById("form-contacto");
const avisoGeneral = document.getElementById("form-contacto-aviso");

const campos = [
    {
        id: "id_nombre",
        validar: valor => (valor === "" || /^\s+$/.test(valor)) ? "Este campo es obligatorio" : ""
    },
    {
        id: "id_correo_electronico",
        validar: valor => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor) ? "" : "Introduce un email válido"
    },
    {
        id: "id_telefono",
        validar: valor => (valor === "" || /^\d{9,10}$/.test(valor)) ? "" : "El teléfono debe tener 9 o 10 dígitos"
    }
];

function mostrarError(campo, mensaje) {
    campo.aviso.textContent = mensaje;
    if (mensaje) {
        campo.elemento.classList.add("campo-error");
    } else {
        campo.elemento.classList.remove("campo-error");
    }
}

function comprobarCampo(campo) {
    const mensaje = campo.validar(campo.elemento.value.trim());
    mostrarError(campo, mensaje);
    return mensaje === "";
}

for (let campo of campos) {
    campo.elemento = document.getElementById(campo.id);
    campo.aviso = document.createElement("span");
    campo.aviso.className = "aviso-error";
    campo.elemento.after(campo.aviso);

    campo.elemento.addEventListener("blur", () => comprobarCampo(campo));
    campo.elemento.addEventListener("focus", () => mostrarError(campo, ""));
}

formulario.addEventListener("submit", event => {
    let valido = true;
    for (let campo of campos) {
        if (!comprobarCampo(campo)) {
            valido = false;
        }
    }

    const privacidad = document.getElementById("id_privacidad");
    if (!privacidad.checked) {
        valido = false;
    }

    if (valido) {
        avisoGeneral.textContent = "";
    } else {
        avisoGeneral.textContent = "Revisa los campos marcados y acepta la política de privacidad.";
        event.preventDefault();
    }
});
