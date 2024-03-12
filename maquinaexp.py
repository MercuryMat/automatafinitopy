alfabeto_figuras = ["A", "C", "P", "G", "0", "1", "2", "X", "O"]
estados = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
estado_ini = "q0"
estado_f = "q6"

def obtener_precio(codigo_producto):
    # Define los precios de los productos
    precios = {
        "C0": 500,
        "C1": 1000,
        "C2": 1500,
        "P0": 500,
        "P1": 1000,
        "P2": 1500,
        "G0": 500,
        "G1": 1000,
        "G2": 1500
    }
    return precios.get(codigo_producto, None)

def transicion(entrada, estado_actual):
    if estado_actual == "q0":
        if entrada == "A":
            return "q1"
    elif estado_actual == "q1":
        if entrada in ["C", "P", "G"]:
            return "q2"
    elif estado_actual == "q2":
        if entrada in ["0", "1", "2"]:
            return "q3"
    elif estado_actual == "q3":
        if entrada in ["X", "O"]:
            return "q4"
    elif estado_actual == "q4":
        return "q5"
    elif estado_actual == "q5":
        return "q6"
    return estado_actual

def validar_monedas(precio, codigo_producto):
    num_monedas = codigo_producto.count("X") * 1000 + codigo_producto.count("O") * 500
    if precio != num_monedas:
        print("La cantidad de monedas ingresada no es correcta.")
        return False
    return True

def main():
    estado_actual = estado_ini
    codigo_producto = ""
    
    entrada_codigo = input("Ingrese el código del producto (A seguido de C, P, o G seguido de 0, 1, o 2): ")
    for entrada in entrada_codigo:
        if entrada not in alfabeto_figuras:
            print("Código de producto inválido.")
            return
        estado_actual = transicion(entrada, estado_actual)
        codigo_producto += entrada
    
    if estado_actual != estado_f:
        print("Código de producto inválido.")
        return

    precio = obtener_precio(codigo_producto)
    if precio is None:
        print("Producto no reconocido.")
        return

    print("El precio del producto es:", precio, "pesos.")

    while True:
        monedas = input("Ingrese las monedas (usando X para 1000 pesos y O para 500 pesos): ")
        if all(moneda in ["X", "O"] for moneda in monedas):
            if validar_monedas(monedas, codigo_producto):
                print("¡Transacción completada exitosamente!")
                return
            else:
                print("La cantidad de monedas ingresada no coincide con el precio del producto.")
        else:
            print("Monedas inválidas, por favor ingrese sólo X y O.")

if __name__ == "__main__":
    main()
