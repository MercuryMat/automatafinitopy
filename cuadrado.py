import turtle

def draw_figure():
    while True:
        input_str = turtle.textinput("Ingrese la figura", "Tipo de figura y tamaño (ejemplo: cuadrado 100):")
        if input_str is None:
            # Si el usuario da clic en "Cancelar" o cierra la ventana, salir del bucle y cerrar el programa
            break

        try:
            turtle.clear()  # Limpiar la pantalla de Turtle

            # Dividir la entrada en tipo y tamaño
            tipo, _, tamaño = input_str.partition(" ")

            # Verificar la validez de la entrada
            if not (tipo and tamaño):
                print("Entrada inválida. Debe ingresar el tipo de figura seguido del tamaño.")
                continue

            tamaño = int(tamaño)
            if tipo.lower() in ('cuadrado', 'triangulo', 'hexagono'):
                dibujar_poligono(tipo.lower(), tamaño)
            elif tipo.lower() == 'circulo':
                dibujar_circulo(tamaño)
            else:
                print("Figura no soportada.")

        except ValueError:
            print("El tamaño debe ser un número entero.")

    # Cerrar la ventana de Turtle
    turtle.bye()

def dibujar_poligono(tipo, tamaño):
    # Determinar el número de lados según el tipo de polígono
    if tipo == 'cuadrado':
        lados = 4
    elif tipo == 'triangulo':
        lados = 3
    elif tipo == 'hexagono':
        lados = 6

    # Dibujar el polígono
    for _ in range(lados):
        turtle.forward(tamaño)
        turtle.left(360 / lados)

def dibujar_circulo(radio):
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()

# Configurar la ventana de Turtle
turtle.setup(width=700, height=700)
turtle.title("Dibujar Figura")

# Llamar a la función principal para empezar el programa
draw_figure()

turtle.done()
