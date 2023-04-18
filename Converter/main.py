valeure_convertie = 0
inch_cm_str = input("1-pouce -> cm   2- cm -> pouce")
try:
    inch_cm = int(inch_cm_str)
except:
    print("ERREUR : veuillez choisir la valeur 1 ou 2")
if inch_cm == 1:
    valeur = input("saisissez la valeur a convertir")
    valeure_convertie = float(valeur) * 2.54
    print(f"resultat est {valeure_convertie} centimetres")
elif inch_cm == 2:
    valeur = input("saisissez la valeur a convertire")
    valeure_convertie = float(valeur) / 2.54
    print(f"resultat est {valeure_convertie} pouces")
