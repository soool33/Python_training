# Questionnaire
def poser_question(question, r1, r2, r3, r4, choix_bonne_reponse):
    global score
    print("Score: ", score)
    print("Question: ")
    print(" ", question)
    print("   (a)", r1)
    print("   (b)", r2)
    print("   (c)", r3)
    print("   (d)", r4)
    print()
    reponse = input("Votre réponse: ")
    if reponse == choix_bonne_reponse:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")
        score -= 1
    print()


score = 10
poser_question("Quelle est la capitale de la france ?", "Marseille", "Nice",
               "Paris", "Bordeaux", "c")
poser_question("Quelle est la capitale de l'italie ?", "Florence", "Rome",
               "Milan", "Venice", "b")

print("Score final: ", score)


# Exercice distance chauffeur ------------------------------------


nom_chauffeur = ["mark", "patrick", "youyou", "zoubir", "moha"]
distance_chauffeur_km = [1.5, 4, 2.6, 0.6, 2.2]


# V2 :

noms_et_distances = [("mark", 1.5), ("patrick", 4), ("youyou", 2.6), ("zoubir", 0.6), ("moha", 2.2)]

nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("Le chauffeur le plus proche est:", nom_et_distance_min[0], ", il se trouve à: ", nom_et_distance_min[1], "km")

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
