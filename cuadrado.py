import turtle

def draw_figure(input_str):
    # Dividimos la cadena en el primer espacio encontrado
    tipo, _, tamaño = input_str.partition(" ")

    # Verificar si se ingresaron tres parámetros
    if not (tipo and tamaño):
        print("Entrada inválida. Debe ingresar el tipo de figura seguido del tamaño.")
        return

    turtle.reset()  # Limpiar la pantalla de Turtle

    # Dibujar la figura en la ventana de Turtle
    try:
        tamaño = int(tamaño)
        if tipo.lower() == 'cuadrado':
            cuadrado(tamaño)
        elif tipo.lower() == 'circulo':
            circulo(tamaño)
        elif tipo.lower() == 'triangulo':
            triangulo(tamaño)
        elif tipo.lower() == 'hexagono':
            hexagono(tamaño)
        else:
            print("Figura no soportada.")
    except ValueError:
        print("El tamaño debe ser un número entero.")

    # Pedir otro comando
    input_str = turtle.textinput("Ingrese la figura", "Tipo de figura y tamaño (ejemplo: cuadrado 100):")
    if input_str:
        draw_figure(input_str)

def cuadrado(lado):
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)

def triangulo(lado):
    for i in range(3):
        turtle.forward(lado)
        turtle.left(120)

def circulo(radio):
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()

def hexagono(lado):
    for i in range(6):
        turtle.forward(lado)
        turtle.left(60)

# Configuración de la ventana de Turtle
turtle.setup(width=700, height=700)
turtle.title("Dibujar Figura")

# Obtener entrada del usuario para la primera figura
input_str = turtle.textinput("Ingrese la figura", "Tipo de figura y tamaño (ejemplo: cuadrado 100):")

if input_str:
    draw_figure(input_str)

turtle.done()
