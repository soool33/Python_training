def tri_perso(e):
    return len(e)


def afficher(collection, n_premiers_elements=-1):
    # collection.sort(reverse=True, key=tri_perso) ----- tri de la selection de pizzas
    c = collection
    if n_premiers_elements != -1:
        c = collection[:n_premiers_elements]

    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("Il n y a aucune pizza a afficher")
        return

    print(f"------------ Liste des pizzas ({nb_pizzas}) ------------")
    for i in c:
        print(i)
    print()
    print("La premiere pizza:", c[0])
    print("La derniere pizza:", c[-1])


def ajouter_pizza(collection):
    p = input("Ajoutez votre pizza: ")
    if p.lower() in collection:
        print("Cette pizza existe deja")
    else:
        collection.append(p)


pizzas = ["4 fromages", "végétarienne", "hawai", "calzon"]
ajouter_pizza(pizzas)
afficher(pizzas, 2)
