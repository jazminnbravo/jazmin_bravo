import random
words = {"programacion" : [
    "python","programa","funcion","bucle"],
    "datos" : ["variable","cadena","entero","lista"],} #Agrupe las palabras segun su categoria (C)

print("¡Bienvenido al Ahorcado!")
print( "Categorias disponibles:") 

for categoria in words: #muestro las categorias disponibles (C)
   print ("-",categoria)

Selec_categoria = input ("Ingresa una categoria: ").lower()  #Pido la categoria (C)

while Selec_categoria not in words: 
    print ("categoria invalida") #control de que existe la categoria (C) 
    Selec_categoria = input ("Ingresa una categoria: ").lower()

word = random.choice(words[Selec_categoria])
guessed = []
attempts = 6 
puntaje = 0 #inicializo

while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress) 
    
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6 #sumas 6 puntos (B)
        print(f"¡Ganaste!,tu puntaje es:{puntaje}")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    letter = input("Ingresá una letra: ").lower()   

    if len(letter) != 1 or not letter.isalpha(): #solo se necesita que se ingrese una letra (A)
        print ("Entrada no valida")
    elif letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1 #restas un punto (B)
        print("Esa letra no está en la palabra")
    print()
else:
    puntaje = 0 #perder te deja en cero puntos (B)
    print(f"¡Perdiste! La palabra era: {word}, tu puntaje queda en {puntaje}")

