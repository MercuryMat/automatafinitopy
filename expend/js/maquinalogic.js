const alfabeto_figuras = ["A", "C", "P", "G", "0", "1", "2", "X", "O"];
const estados = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"];
const estado_ini = "q0";
const estado_f = "q6";

function obtener_precio(codigo_producto) {
    // Define los precios de los productos
    const precios = {
        "C0": 500,
        "C1": 1000,
        "C2": 1500,
        "P0": 500,
        "P1": 1000,
        "P2": 1500,
        "G0": 500,
        "G1": 1000,
        "G2": 1500
    };
    return precios[codigo_producto] || null;
}

function transicion(entrada, estado_actual) {
    switch (estado_actual) {
        case "q0":
            return entrada === "A" ? "q1" : estado_actual;
        case "q1":
            return entrada.match(/[C|P|G]/) ? "q2" : estado_actual;
        case "q2":
            return entrada.match(/[0-2]/) ? "q3" : estado_actual;
        case "q3":
            return entrada.match(/[X|O]/) ? "q4" : estado_actual;
        case "q4":
            return "q5";
        default:
            return estado_actual;
    }
}

function main() {
    let estado_actual = estado_ini;
    let codigo_producto = "";

    // Obtener entrada del usuario
    const entrada = document.getElementById("entrada").value.toUpperCase();
    let esProducto = false;
    for (let i = 0; i < entrada.length; i++) {
        const caracter = entrada[i];
        if (!alfabeto_figuras.includes(caracter)) {
            alert("Entrada inválida.");
            return;
        }
        if (!esProducto && caracter === "A") {
            esProducto = true;
        }
        estado_actual = transicion(caracter, estado_actual);
        codigo_producto += caracter;
    }

    // Validar el estado final
    if (!esProducto || estado_actual !== estado_f) {
        alert("Estado final inválido.");
        return;
    }

    // Obtener y mostrar el precio del producto
    const precio = obtener_precio(codigo_producto);
    if (precio === null) {
        alert("Producto no reconocido.");
        return;
    }
    alert(`El precio del producto ${codigo_producto} es: ${precio} pesos.`);

    // Proceso de pago
    let pagoCorrecto = false;
    while (!pagoCorrecto) {
        const pago = prompt("Ingrese el pago usando 'X' para 500 pesos y 'O' para 1000 pesos: ");
        const cantidadX = (pago.match(/X/g) || []).length;
        const cantidadO = (pago.match(/O/g) || []).length;
        const totalPago = cantidadX * 500 + cantidadO * 1000;
        if (totalPago === precio) {
            pagoCorrecto = true;
            alert("¡Pago exitoso!");
        } else if (totalPago < precio) {
            alert("La cantidad de dinero es insuficiente. Añada más monedas.");
        } else {
            alert("El pago excede el precio del producto. Retire algunas monedas.");
        }
    }
}