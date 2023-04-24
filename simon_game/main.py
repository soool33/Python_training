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

while True:
    print("retenez la sequence")
    time.sleep(1)
    print(sequence)
    time.sleep(3)
    clear_screen()
