import random
import os
import time


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


sequence = ""
for i in range(4):
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)

clear_screen()
print("Bienvenue au jeu du simon")

score = 0
while True:
    print("retenez la sequence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()

    sequence_user = input("Votre réponse: ")
    if sequence_user == sequence:
        score += 1
    else:
        break

    print(f"votre score est: {score}")
    chiffre = random.randint(0, 9)
    sequence += str(chiffre)
    clear_screen()

print("Mauvaise reponse")
print(f"La sequence était: {sequence}")
print(f"votre score final est: {score}")


# Exo: Table de multiplications

# def afficher_table_multiplication(n: int, min, max):
#     if min > max:
#         print("ERREUR: le min est superieur au max")
#         return
#     for i in range(min, max+1):
#         print(i, "x", n, "=", i*n)
#     print("-----FIN-----")
#
#
# afficher_table_multiplication(7, 5, 9)
