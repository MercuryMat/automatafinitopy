import turtle

alfabeto_automata = "G"
alfabeto_figuras = ["C", "T", "R", "H"]

estados_cuadrado = ["Q0", "Q1", "Q2", "Q3", "Q4"]
estados_triangulo = ["Q0", "Q5", "Q6", "Q7"]
estados_rombo = ["Q0", "Q8", "Q9", "Q10", "Q11"]
estados_hexagono = ["Q0", "Q12", "Q13", "Q14", "Q15", "Q16", "Q17"]

turtle.speed(10)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

def dibujar_cuadrado(tamaño):
    estado_actual = "Q0"
    for estado in estados_cuadrado[1:]:
        print(f"Ir de {estado_actual} a {estado}: ")
        if estado == "Q1":
            turtle.forward(tamaño)
        elif estado == "Q2":
            turtle.right(90)
            turtle.forward(tamaño)
        elif estado == "Q3":
            turtle.right(90)
            turtle.forward(tamaño)
        elif estado == "Q4":
            turtle.right(90)
            turtle.forward(tamaño)
        estado_actual = estado
    print(f"El estado de aceptacion  es: {estado_actual}")

def dibujar_triangulo(tamaño):
    estado_actual = "Q0"
    for estado in estados_triangulo[1:]:
        print(f"Ir de {estado_actual} a {estado}: ")
        if estado == "Q5":
            turtle.forward(tamaño)
        elif estado == "Q6":
            turtle.left(120)
            turtle.forward(tamaño)
        elif estado == "Q7":
            turtle.left(120)
            turtle.forward(tamaño)
        estado_actual = estado
    print(f"El estado de aceptacion  es: {estado_actual}")

def dibujar_rombo(tamaño):
    estado_actual = "Q0"
    for estado in estados_rombo[1:]:
        print(f"Ir de {estado_actual} a {estado}: ")
        if estado == "Q8":
            turtle.left(60)
            turtle.forward(tamaño)
        elif estado == "Q9":
            turtle.left(60)
            turtle.forward(tamaño)
        elif estado == "Q10":
            turtle.left(120)
            turtle.forward(tamaño)
        elif estado == "Q11":
            turtle.left(60)
            turtle.forward(tamaño)
        estado_actual = estado
    print(f"El estado de aceptacion  es: {estado_actual}")

def dibujar_hexagono(tamaño):
    estado_actual = "Q0"
    for estado in estados_hexagono[1:]:
        print(f"Ir de {estado_actual} a {estado}: ")
        if estado == "Q12":
            turtle.forward(tamaño)
        elif estado == "Q13":
            turtle.left(60)
            turtle.forward(tamaño)
        elif estado == "Q14":
            turtle.left(60)
            turtle.forward(tamaño)
        elif estado == "Q15":
            turtle.left(60)
            turtle.forward(tamaño)
        elif estado == "Q16":
            turtle.left(60)
            turtle.forward(tamaño)
        elif estado == "Q17":
            turtle.left(60)
            turtle.forward(tamaño)
        estado_actual = estado
    print(f"El estado de aceptacion  es: {estado_actual}")

while True:
    turtle.reset()  
    automata = input("Ingrese el automata: ")
    if automata.lower() == alfabeto_automata.lower():
        figura = input("Ingrese siguiente patron: ")
        if figura.upper() in alfabeto_figuras:
            while True:
                tamaño = input("Ingrese el tamaño de la figura (mínimo 50, máximo 200): ")
                if tamaño.isdigit() and 50 <= int(tamaño) <= 200:
                    tamaño = int(tamaño)
                    break
                else:
                    print("El tamaño ingresado no es válido. Debe ser un número entre 50 y 200.")
            if figura.upper() == "C":
                dibujar_cuadrado(tamaño)
            elif figura.upper() == "T":
                dibujar_triangulo(tamaño)
            elif figura.upper() == "R":
                dibujar_rombo(tamaño)
            elif figura.upper() == "H":
                dibujar_hexagono(tamaño)
            else:
                print("La figura ingresada no pertenece a las opciones disponibles.")
        else:
            print("La figura ingresada no pertenece al alfabeto de este autómata.")
    else:
        print("El automata ingresado no pertenece a un lenguaje automata finito")

    while True:
        reiniciar = input("¿Desea dibujar otra figura? (S/N): ")
        if reiniciar.lower() in ['s', 'n']:
            break
        else:
            print("Ingrese una opción válida (S para sí, N para no).")
    if reiniciar.lower() == "n":
        break
turtle.bye()
