"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
11/12/2024

Exercice de code : Affichage d'un Sapin
Ecrire un programme qui attend dans cet ordre un entier
N >= 2 et un caractère d'affichage puis qui affiche le
sapin suivant :
si Hauteur du sapin = 5 et Caractère du sapin = * alors
affiche =
Hauteur du sapin : 5
Caractère du sapin : *
   *
  ***
 *****
*******
   *
"""


# Initialisation des variables "hauteur" et "espace"
hauteur = 0
espace = " "

# Boucle qui vérifie que la valeur entrée est bien suppérieur ou égale à 2
while hauteur < 2:
    # Demande la hauteur souhaité pour le sapin
    hauteur = int(input("Saisissez une hauteur (>= 2) : "))

# Demande le caractère dont est composé le sapin
caractere = str(input("Caractère du sapin : "))

# Boucle dont le nombre d'itération correspond à la hauteur moins 1 (afin d'ensuite ajouter le pied du sapin)
for i in range(hauteur - 1):
    # Affiche une ligne du sapin en ajoutant des espaces, puis le caractère (le nombre de fois nécessaire)
    print(espace * (hauteur - i - 1) + caractere * (2 * i + 1))
# Affiche le pied du sapin (en mettant des espaces avant)
print(espace * (hauteur - 1) + caractere)