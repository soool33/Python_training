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
