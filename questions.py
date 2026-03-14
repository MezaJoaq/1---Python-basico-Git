import random
categoria = {
    "Conceptos" : ["python","programa"],
    "Estructuras" : ["funcion","bucle"],
    "Datos" : ["cadena","entero","lista"],
    "Sintaxis" : ["variable"]
}
menu = """ 
//////////////////////////////////////
    ¡BIENVENIDO AL AHORCADO!
//////////////////////////////////////
Seleccione una categoria
    1- Conceptos
    2- Estructuras
    3- Datos
    4- Sintaxis
--------------------------------------
Ingrese su opcion (1-4):
"""
#Menu de opciones de categoria, se elige un valor aleatorio 
opcion = input(menu)
match opcion:
    case "1":
        word = (categoria["Conceptos"][random.randint(0,1)])
    case "2":
        word = (categoria["Estructuras"][random.randint(0,1)])
    case "3":
        word = (categoria["Datos"][random.randint(0,2)])
    case "4":
        word = (categoria["Sintaxis"][0])
    case _:            #Si se ingresa un caracter distinto se asigna la categoria conceptos
        print('Se asigno la categoria Conceptos')
        word = (categoria["Conceptos"][random.randint(0,1)])

guessed = []
attempts = 6
score = 0


while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
            print(progress)# Verificar si el jugador ya adivinó la palabra completa

    if "_" not in progress:
        score += 6
        print("¡Ganaste!")
        print(f"Tu puntaje es {score}")
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ")
    # Comprueba el rango y si el caracter ingresa es una letra
    if len(letter) >= 2 or not letter.isalpha():
        print("Entrada no valida")
    else:
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
            print()
else:
    score = 0
    print(f"¡Perdiste! La palabra era: {word}")
    print(f"Tu puntaje es {score}")