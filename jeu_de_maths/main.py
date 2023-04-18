import random

MIN_NUM = 1
MAX_NUM = 10
NB_QESTION = 4


def poser_question():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    o = random.randint(0, 1)

    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    reponse_str = input(f"Calculez : {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a + b
    if o == 1:
        calcul = a * b
    if reponse_int == calcul:
        # print("Reponse correcte :-)")
        return True

        # print("Reponse incorrecte :-(")
    return False


nb_points = 0
for i in range(0, NB_QESTION):
    print(f"Question n°{i + 1} sur {NB_QESTION} :")
    if poser_question():
        print("Reponse correcte :-)")
        nb_points += 1
    else:
        print("Reponse incorrecte :-(")
    print()

print(f"Vous avez {nb_points}/{NB_QESTION} bonnes reponses")
if nb_points / NB_QESTION == 1:
    print("Resultat parfait, excellent")
elif nb_points / NB_QESTION == 0:
    print("Aucune bonne réponse, revisez vos maths !!!")
elif 1 > nb_points / NB_QESTION >= 0.5:
    print("Vous avez la moyenne")
elif 0 < nb_points / NB_QESTION <= 0.5:
    print("Vous n'avez pas la moyenne, vous devez vous ameliorer")
