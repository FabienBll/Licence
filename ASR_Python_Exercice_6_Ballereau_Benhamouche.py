"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
11/12/2024

Exercice 6
Ecrire un programme qui attend un entier puis qui
affiche sa table de multiplication.
Ensuite, on entre de nouveau un entier puis on affiche
sa table et ainsi de suite jusqu'à ce que l'entier entré
soit égal à-1.
Quand on rencontre l'entier -1, le programme s'arrête
(sans afficher la table de -1).
Une ligne vierge sépare deux tables affichées comme le
montre l'exemple ci-dessous pour lequel l’entiers entrés
est 16.
16 x 1 = 16
16 x 2 = 32
"""

# Initialisation de la variable entier
entier = 0

# Boucle permettant de demander un entier tant que celui-ci n'est pas égale à -1
while entier != -1:

    # Saisie utilisateur d'un entier
    entier = int(input("Quelle nouvelle table de multiplication voulez-vous afficher ? (-1 pour quitter)"))

    # Si l'entrée n'est pas égale à -1 alors il affiche sa table de multiplication
    if entier != -1:
        # Boucle affichant la table de multiplication (en ajoutant 1 à i à chaque itération)
        for i in range(10):
            print(entier, "x", i+1, "=", entier*(i+1))
        # Une ligne vierge sépare les deux tables affichées
        print("")