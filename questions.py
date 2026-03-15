import random

categoria = {
    "Conceptos": ["python", "programa"],
    "Estructuras": ["funcion", "bucle"],
    "Datos": ["cadena", "entero", "lista"],
    "Sintaxis": ["variable"],
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
reintento = True


while reintento == True:
    # Menu de opciones de categoria
    opcion = input(menu)
    match opcion:
        case "1":
            eleccion = categoria["Conceptos"]
        case "2":
            eleccion = categoria["Estructuras"]
        case "3":
            eleccion = categoria["Datos"]
        case "4":
            eleccion = categoria["Sintaxis"]

        # Si se ingresa un caracter distinto se asigna la categoria conceptos
        case _:
            print("Se asigno la categoria Conceptos")
            eleccion = categoria["Conceptos"]

    cont = True
    pos = 0

    # Toma la cantidad de elementos y devuelve una lista con los mismos valores pero mezclada.
    cant_elementos = len(eleccion)
    mezcla = random.sample(eleccion, cant_elementos)
    while cont and pos < cant_elementos:
        word = mezcla[pos]
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
                    print(
                        progress
                    )  # Verificar si el jugador ya adivinó la palabra completa

            if "_" not in progress:
                score += 6
                print("¡Ganaste!")
                print(f"Tu puntaje es {score}")
                pos += 1
                opc = int(
                    input("¿Quieres continuar? (0 = No continuar ---- 1 = Continuar)")
                )
                if opc != 1:
                    cont = False
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
            pos += 1
            opc = int(
                input("¿Quieres continuar? (0 = No continuar ---- 1 = Continuar)")
            )
            if opc != 1:
                cont = False
        if not cont or pos >= cant_elementos:
            opc = int(
                input(
                    "¿Quieres continuar jugando con otra categoria? (0 = No continuar ---- 1 = Continuar)"
                )
            )
            if opc != 1:
                reintento = False
