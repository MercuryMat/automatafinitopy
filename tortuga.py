import turtle

# Crear una ventana de dibujo
ventana = turtle.Screen()
ventana.setup(500, 500)

# Crear una tortuga
tortuga = turtle.Turtle()

# Definir la posición inicial de la tortuga
posicion_x = 0
posicion_y = 0
tortuga.penup()
tortuga.goto(posicion_x, posicion_y)
tortuga.pendown()

# Definir el tamaño del paso y el ángulo de giro
paso = 50
angulo = 90

# Definir el diccionario de movimiento
movimientos = {
    "adelante": 2,
    "este": 1,
    "oeste": 1,
}

# Mover la tortuga según los comandos del usuario
while True:
    comando = input("Introduzca un comando (adelante, este, oeste) o 'salir' para terminar: ")
    
    if comando == "salir":
        break
    
    if comando not in movimientos:
        print("Comando inválido")
        continue
    
    repeticiones = int(input("Introduzca la cantidad de repeticiones: "))
    
    for i in range(repeticiones):
        if comando == "adelante":
            tortuga.forward(paso)
            posicion_y += paso
        elif comando == "este":
            tortuga.left(angulo)
        elif comando == "oeste":
            tortuga.right(angulo)
        
        # Imprimir la posición actual de la tortuga
        print(f"La tortuga está en la posición ({posicion_x}, {posicion_y})")

# Esperar a que el usuario cierre la ventana
turtle.done()