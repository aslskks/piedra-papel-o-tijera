import random
import time
gana_jugador = 0
gana_pc = 0
lista =["piedra", "papel", "tijera"]
while True:
    if gana_jugador > gana_pc:
        print("va ganando la pc")
    elif gana_jugador < gana_pc:
        print("la pc va ganando")
    elif gana_jugador == gana_pc:
        print("van en Empate")
    elif (gana_jugador == 0 and gana_pc == 0):
        print("van 0 a 0")
    user = input("Elija: piedra, papel, tijera: ")
    if user not in lista:
        print("Esa opcion no existe")
        continue
    pc = random.choice(lista)
    print(f"PC: {pc}")
    
    if user == pc:
        print(f"Empate, ambos elijieron {pc}")
    
    elif (user == "piedra" and pc == "tijera") or (user == "tijera" and pc == "papel") or (user == "papel" and pc == "piedra"):
        print("gana el jugador")
        gana_jugador += 1
        continue
    else:
        print("gana el pc")
        gana_pc += 1
        continue