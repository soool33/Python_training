# LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

def extraire_extension(nom_fichier):
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) <= 1:
        return None
    return nom_fichier_split[-1]


def obtenir_definition_extension(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
    return None


fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning",
            "data.dat")

definition_extensions = (("doc", "Document Word"),
                         ("exe", "Executable"),
                         ("txt", "Document Texte"),
                         ("jpeg", "Image JPEG"))

for fichier in fichiers:
    ext = extraire_extension(fichier)
    if ext:
        definition = obtenir_definition_extension(ext, definition_extensions)
        if not definition:
            definition = "Extension non connue"
    else:
        definition = "Aucune extention"
    print(fichier + " ( " + definition + " ) ")
