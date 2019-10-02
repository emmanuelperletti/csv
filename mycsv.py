import csv

with open("ged.csv", "r") as f:
    contenu_fichier = csv.DictReader(f, delimiter=";")
    print(contenu_fichier.line_num)

    for ligne in contenu_fichier:
        for rubrique in ligne:
            print(f"{rubrique} : {ligne[rubrique]}")

