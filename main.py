import random

print("Bienvenido a NUMBER GUESSING\nAdivina el numero que piensa la Computadora"
" Debera ser entre 0 y 10. Y recuerda que tienes 3 intentos")

numero_a_adivinar = random.randint(0, 10)
#print(numero_a_adivinar)

while True:
    try:
        numero_usuario = int(input("Ingresa tu numero:"))
        break
    except:
        print("Por favor ingrese un numero.")

contador = 3

while numero_usuario < 0 or numero_usuario > 10:
    print("Ingresa un numero entre 0 y 10")
    try:
        numero_usuario = int(input("Ingresa tu numero:"))
    except:
        print("Por favor ingrese un numero entero.")

while contador >= 0:

    if numero_usuario == numero_a_adivinar:
        print("Felicitaciones!! Has adivinado.")
        break
    elif numero_usuario > numero_a_adivinar and numero_usuario < 10:
        print("Su numero es mayor que el de la Computadora")
    elif numero_usuario < numero_a_adivinar and numero_usuario > 0:
        print("Su numero es menor que el de la Computadora")
    else:
        print("Recuerde que su numero debe ser entre 0 y 10")

    print(f"Te quedan {contador - 1} intentos.")

    contador -= 1

    if contador == 0:
        print("Lo siento, no has adivinado.")
        break
    
    while True:
        try:    
            numero_usuario = int(input("Ingresa tu numero:"))
            break
        except:
            print("Por favor ingrese un numero entero.")