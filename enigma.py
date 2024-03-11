import string

# Definimos el alfabeto y los rotores utilizados por la Enigma
alphabet = string.ascii_uppercase
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

# Definimos la posición inicial de los rotores
position1 = "X"
position2 = "C"
position3 = "R"

# Definimos la configuración inicial de los enchufes
plugs = {
    "A": "M",
    "B": "N",
    "C": "O",
    "D": "P",
    "E": "Q",
    "F": "R",
    "G": "S",
    "H": "T",
    "I": "U",
    "J": "V",
    "K": "W",
    "L": "X",
    "M": "A",
    "N": "B",
    "O": "C",
    "P": "D",
    "Q": "E",
    "R": "F",
    "S": "G",
    "T": "H",
    "U": "I",
    "V": "J",
    "W": "K",
    "X": "L",
    "Y": "Y",
    "Z": "Z"
}

# Definimos el reflector
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def enigma(message):
    # Convertimos las variables de posicion en globales
    global position1, position2, position3

    # Convertimos el mensaje a mayúsculas
    message = message.upper()

    # Inicializamos la salida
    output = ""

    # Para cada letra del mensaje
    for letter in message:
        # Si la letra está en el alfabeto
        if letter in alphabet:
            # Movemos los rotores
            position3 = alphabet[(alphabet.index(position3) + 1) % len(alphabet)]
            if alphabet.index(position3) == alphabet.index("R"):
                position2 = alphabet[(alphabet.index(position2) + 1) % len(alphabet)]
            if alphabet.index(position2) == alphabet.index("F"):
                position1 = alphabet[(alphabet.index(position1) + 1) % len(alphabet)]

            # Pasamos la letra por los enchufes
            if letter in plugs:
                letter = plugs[letter]

            # Pasamos la letra por el primer rotor
            index = alphabet.index(letter)
            letter = rotor1[(index + alphabet.index(position1)) % len(alphabet)]
            index = (index + alphabet.index(position1)) % len(alphabet)

            # Pasamos la letra por el segundo rotor
            letter = rotor2[(index + alphabet.index(position2)) % len(alphabet)]
            index = (index + alphabet.index(position2)) % len(alphabet)

            # Pasamos la letra por el tercer rotor
            letter = rotor3[(index + alphabet.index(position3)) % len(alphabet)]
            index = (index + alphabet.index(position3)) % len(alphabet)

            # Pasamos la letra por el reflector
            letter = reflector[index]

            # Pasamos la letra por el tercer rotor en sentido inverso
            index = (alphabet.index(letter) - alphabet.index(position3)) % len(alphabet)
            letter = alphabet[(index - alphabet.index(position3)) % len(alphabet)]

            # Pasamos la letra por el segundo rotor en sentido inverso
            index = (alphabet.index(letter) - alphabet.index(position2)) % len(alphabet)
            letter = alphabet[(index - alphabet.index(position2)) % len(alphabet)]

            # Pasamos la letra por el primer rotor en sentido inverso
            index = (alphabet.index(letter) - alphabet.index(position1)) % len(alphabet)
            letter = alphabet[(index - alphabet.index(position1)) % len(alphabet)]

            # Pasamos la letra por los enchufes de nuevo
            if letter in plugs:
                letter = plugs[letter]

            # Agregamos la letra a la salida
            output += letter

    return output

cifrado = enigma("Enigma")
print(cifrado)