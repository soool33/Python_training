# Questionnaire

def demander_reponse_numerique_utilisateur(min, max):
    reponse_str = input(f"Votre réponse(entre {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR: Vous devez entrez un nombre entre", min, "et", max)
    except:
        print("ERREUR: Vous devez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utilisateur(min, max)


def poser_question(question):
    choix = question[1]
    bonne_reponse = question[2]
    global score
    # print("Score: ", score)
    print("Question: ")
    print(" ", question[0])
    for i in range(len(choix)):
        print("   ", i + 1, "-", choix[i])

    print()
    reponse_int = demander_reponse_numerique_utilisateur(1, len(choix))

    if choix[reponse_int - 1].lower() == bonne_reponse.lower():
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        score -= 1
    print()


score = 0


def lancer_questionnaire(questionnaire):
    for question in questionnaire:
        poser_question(question)


questionnaire_capitale = (
    ("Quelle est la capitale de la france ?", ("Marseille", "Nice", "Paris", "Bordeaux", "Lille"), "Paris"),
    ("Quelle est la capitale de l'italie ?", ("Florence", "Rome", "Milan", "Venice"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruges", "Bruxelles", "Liege"), "Bruxelles")
)

lancer_questionnaire(questionnaire_capitale)

print("Score final: ", score)

# Exercice distance chauffeur ------------------------------------


# nom_chauffeur = ["mark", "patrick", "youyou", "zoubir", "moha"]
# distance_chauffeur_km = [1.5, 4, 2.6, 0.6, 2.2]
#
#
# # V2 :
#
# noms_et_distances = [("mark", 1.5), ("patrick", 4), ("youyou", 2.6), ("zoubir", 0.6), ("moha", 2.2)]
#
# nom_et_distance_min = noms_et_distances[0]
# for nom_et_distance in noms_et_distances:
#     if nom_et_distance[1] < nom_et_distance_min[1]:
#         nom_et_distance_min = nom_et_distance
#
# print("Le chauffeur le plus proche est:", nom_et_distance_min[0], ", il se trouve à: ", nom_et_distance_min[1], "km")

# V1 :

# index_min = 0
# distance_min = distance_chauffeur_km[0]
# for i in range(len(distance_chauffeur_km)):
#     distance = distance_chauffeur_km[i]
#     if distance < distance_min:
#         distance_min = distance
#         index_min = i
#
# print("La distance minimale est: ", distance_min)
# print("index de la distance minimale: ", index_min)
# print("Le chauffeur le plus proche ets:", nom_chauffeur[index_min])
