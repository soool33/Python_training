import time
import beepy

print("Programme de temps de cuisson des oeufs")
print("1- Oeufs à la coque")
print("2- Oeufs mollets")
print("3- Oeufs durs\n")
while True:
    choix = input("Choisissez 1 2 ou 3 ")
    if choix == "1" or choix == "2" or choix == "3":
        break
    print("ERREUR: vous devez choisir 1, 2 ou 3\n")

duree = 0
if choix == "1":
    duree = 3 * 60
if choix == "2":
    duree = 6 * 60
if choix == "3":
    duree = 9 * 60

while True:
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
        duree -= 1
        if duree <= 0:
            break

    if duree <= 0:
        break
    min = duree // 60  # division entiere (pas de virgule)
    sec = duree - min * 60
    print()
    print(f"Temps restant : {min:02d}:{sec:02d}", end="", flush=True)

print()
print("Cuisson terminée")
beepy.beep(sound="ping")
