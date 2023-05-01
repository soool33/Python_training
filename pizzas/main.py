def afficher(collection):
    print(f"------------ Liste des pizzas ({len(collection)}) ------------")
    for i in collection:
        print(i)


pizzas = ("4 fromages", "végétarienne", "hawai", "calzon")
afficher(pizzas)