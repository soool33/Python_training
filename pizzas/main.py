def afficher(collection):
    nb_pizzas = len(collection)
    if nb_pizzas == 0:
        print("Il n y a aucune pizza a afficher")
        return

    print(f"------------ Liste des pizzas ({nb_pizzas}) ------------")
    for i in collection:
        print(i)
    print()
    print("La premiere pizza:", collection[0])
    print("La derniere pizza:", collection[-1])


def ajouter_pizza(collection):
    p = input("Ajoutez votre pizza: ")
    collection.append(p)


pizzas = ["4 fromages", "végétarienne", "hawai", "calzon"]
ajouter_pizza(pizzas)
afficher(pizzas)
