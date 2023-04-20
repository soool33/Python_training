import time


def minuteur(durée: int):
    min = durée // 60
    sec = durée - min * 60
    print(f"{min:02d} min")
    print(f"{sec:02d} sec")


print("Programme de temps de cuisson des oeufs")
print("1- Oeufs à la coque")
print("2- Oeufs mollets")
print("3- Oeufs durs\n")

choix = input("Choisissez 1 2 ou 3 ")
if choix == "1":
    minuteur(90)
if choix == "2":
    minuteur(120)
if choix == "3":
    minuteur(150)
