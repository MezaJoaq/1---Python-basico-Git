import random
words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]
word = random.choice(words)
guessed = []
attempts = 6
score = 0

print("¡Bienvenido al Ahorcado!")
print()

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