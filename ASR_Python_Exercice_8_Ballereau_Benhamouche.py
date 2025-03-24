"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
11/12/2024

Ecrire un programme qui attend une liste L d'entiers et qui affiche les effectifs
cumulés des différents éléments de la liste sous forme de bâtons constitués d'étoiles.
Par exemple, si L = [13 , 15 , 12 , 17 , 15 , 18 , 15 , 17 , 13 , 12 , 15 ] , le programme
affiche :
**12
**13
****15
**17
*18
On affichera les éléments de la liste dans l'ordre croissant
On entrera successivement :
le nombre de valeurs de la liste,
les valeurs de la liste
"""

# Saisie utilisateur du nombre de valeurs dans la liste
nbr_valeur = int(input("Nombre de Valeur dans la liste : "))
liste = []

# Boucle permettant la saisie utilisateur des valeurs de la liste (le nombre de fois souhaité)
for i in range(nbr_valeur):
    valeur = int(input(f"Valeur N° {i + 1} : "))
    liste.append(valeur)

# Trie de la liste
liste.sort()

# Compte le nombre de fois qu'apparait chaque valeur dans la liste
compte = {}
for valeur in liste:
    if valeur in compte:
        compte[valeur] += 1
    else:
        compte[valeur] = 1

# Affiche les effectifs cumulé ainsi que leur nombre d'apparition sous forme d'étoiles (placées juste avant)
for valeur, nombre in compte.items():
    print('*' * nombre + str(valeur))