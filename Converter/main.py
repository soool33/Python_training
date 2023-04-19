# def converter_choice():
#     inch_cm = 0
#     while inch_cm == 0:
#         inch_cm_str = input("1-pouce -> cm   2-cm -> pouce ")
#         try:
#             inch_cm = int(inch_cm_str)
#         except:
#             print("ERREUR : veuillez entrer un nombre valide")
#         else:
#             if inch_cm > 2 or inch_cm < 0:
#                 print("ERREUR : veuillez choisir entre 1 et 2")
#                 inch_cm = 0
#     return inch_cm
#
#
# choix = converter_choice()
#
# valeur_flt = 0
# while valeur_flt == 0:
#     valeur_str = input("saisissez la valeur a convertir")
#     try:
#         valeur_flt = float(valeur_str)
#     except:
#         print("ERREUR : La valeure a convertire doit etre un nombre")
#         valeur_flt = 0
#         print("")
#     else:
#         if choix == 1:
#             valeure_convertie = round(valeur_flt * 2.54, 2)
#             print(f"resultat est {valeure_convertie} centimetres")
#         else:
#             valeure_convertie = round(valeur_flt / 2.54, 2)
#             print(f"resultat est {valeure_convertie} pouces")


# fonction de la conversion
def convert(unit1: str, unit2: str, facteur: float):
    valeur_str = input(f"Conversion {unit1} -> {unit2}. Donnez la valeur en {unit1} (ou 'q' pour quiter)")
    if valeur_str == "q":
        return True
    try:
        valeur_flt = float(valeur_str)
    except ValueError:
        print("ERREUR : La valeure a convertire doit etre un nombre")
        print("Utilisez les points et non les virgules pour les décimales")
        print("")
        return convert(unit1, unit2, facteur)

    valeur_convertie = round(valeur_flt * facteur, 2)
    print(f"Resultat de la conversion : {valeur_flt} {unit1} = {valeur_convertie} {unit2}")
    return False


while True:
    print("convertisseur d'unités")
    print("1 - Pouces vers Cm")
    print("2 - Cm vers Pouces")
    print("")
    choix = input("Choisissez 1 ou 2 ")
    if choix == "1" or choix == "2":
        break
    print("ERREUR : vous devez choisir entre 1 et 2 ")
    print("")

while True:
    if choix == "1":
        if convert("Pouces", "Cm", 2.54):
            break
    if choix == "2":
        if convert("Cm", "Pouces", 0.394):
            break
