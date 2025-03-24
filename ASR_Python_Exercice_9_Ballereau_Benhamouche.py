"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
11/12/2024

Ecrire un programme qui attend une liste L de
chaines de caractères et une voyelle V et qui
supprime de la liste L toutes les chaines contenant la
voyelle V.
On entrera successivement :
le nombre de valeurs de la liste,
les valeurs de la liste,
la voyelle V.
Puis le programme affichera la liste finale au format
habituel.
On attend simplement l'instruction print (L)
"""

# Déclaration fonction "est_voyelle", prend en entrée : caractere
# Vérifie si le caractère donné est une voyelle (minuscule ou majuscule)
def est_voyelle(caractere):
    voyelles = "aeiouAEIOU"
    return caractere in voyelles

# Déclaration fonction "supprimer_mots_avec_voyelle", prend en entrée : liste, voyelle
# Supprime les mots de la liste contenant la voyelle donnée
def supprimer_mots_avec_voyelle(liste, voyelle):

    # Convertit la voyelle en minuscule pour la comparaison
    voyelle = voyelle.lower()

    # Retourne une nouvelle liste ne contenant que les mots sans la voyelle spécifiée
    return [mot for mot in liste if voyelle not in mot.lower()]

# Demande à l'utilisateur d'entrer le nombre de valeurs dans la liste
nbr_valeurs = int(input("Nombre de valeurs dans la liste : "))

# Initialise une liste vide pour stocker les valeurs
liste = []

# Demande à l'utilisateur de saisir les valeurs de la liste
for i in range(nbr_valeurs):
    valeur = input(f"Valeur N° {i + 1} : ")
    liste.append(valeur)

# Demande à l'utilisateur de saisir une voyelle valide
voyelle = ""

# Boucle vérifiant que la saisie est une voyelle valide
while not (len(voyelle) == 1 and est_voyelle(voyelle)):
    voyelle = input("Saisissez une voyelle : ")

    # Condition qui signale à l'utilisateur si ce n'est pas une voyelle
    if not est_voyelle(voyelle):
        print(voyelle, "n'est pas une voyelle. Veuillez réessayer.")

# Applique la suppression des mots contenant la voyelle
liste_finale = supprimer_mots_avec_voyelle(liste, voyelle)

# Affiche la liste finale après suppression
print(liste_finale)