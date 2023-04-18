import random


def demander_nombre(min_num, max_num):
    num_int = 0
    while num_int == 0:
        num_str = input(f"Quel est le nombre magique (entre {min_num} et {max_num})")
        try:
            num_int = int(num_str)
        except:
            print("ERREUR: veuillez entrer un nombre valide")
        else:
            if num_int < min_num or num_int > max_num:
                print(f"Erreur : Le nombre doit etre entre {min_num} et {max_num}, try again")
                num_int = 0
    return num_int


MIN_NUM = 1
MAX_NUM = 10
MAGIC_NUM = random.randint(MIN_NUM, MAX_NUM)
NB_LIVES = 3

""" Version 1
number = 0
life = NB_LIVES
while not number == MAGIC_NUM and life > 0:
    print(f"il vous reste {life} vies")
    number = demander_nombre(MIN_NUM, MAX_NUM)
    if number == MAGIC_NUM:
        print("Bravo")
    elif number > MAGIC_NUM:
        print("le nombre magique est plus petit")
        life -= 1
    else:
        print("le nombre magique est plus grand")
        life -= 1
if life == 0:
    print(f"Vous avez perdu :-(, le nombre magique était {MAGIC_NUM}")"""

win = False
for i in range(0, NB_LIVES):
    life = NB_LIVES - i
    print(f"il vous reste {life} vies")
    number = demander_nombre(MIN_NUM, MAX_NUM)
    if number == MAGIC_NUM:
        print("Bravo, vous avez gagné")
        win = True
        break
    elif number > MAGIC_NUM:
        print("le nombre magique est plus petit")
    else:
        print("le nombre magique est plus grand")
if not win:
    print(f"Vous avez perdu :-(, le nombre magique était {MAGIC_NUM}")
