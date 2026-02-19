#emojies backup ✊​✋​✌️​
import random

print("Piedra Papel o Tijeras")

#input

print("Elige:")
print("1. Piedra")
print("2. Papel")
print("3. Tijeras")

User = int(input())

Machine = random.randint(1,3)

#procesing

print("Resultados")
if User == 1:
    if Machine == 1:
        print("✊​ / ✊​")
        print("Empate")
    elif Machine == 2:
        print("✊​ / ✋​")
        print("Perdiste")
    else:
        print("✊ / ✌️​")
        print("Ganaste")
elif User == 2:
    if Machine == 1:
        print("✋ / ✊​​")
        print("Ganaste")
    elif Machine == 2:
        print("✋ / ✋​")
        print("Empate")
    else:
        print("✋ / ✌️​")
        print("Perdiste")
elif User == 3:
    if Machine == 1:
        print("✌️​ / ✊​")
        print("Perdiste")
    elif Machine == 2:
        print("✌️ / ✋​​")
        print("Ganaste")
    else:
        print("✌️ / ✌️​​")
        print("Empate")
else:
    print("ERROR!: Elección no valida")
    exit()

#output

print("---------------------------------")