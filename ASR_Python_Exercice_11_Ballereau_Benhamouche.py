"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
08/01/2025

Ecrire un programme qui affiche un dictionnaire en partant du mot dont la définition est la plus
longue, puis en ordonnant les mots dans l'ordre des définitions décroissantes.
On considère un "vrai" dictionnaire nommé Dico, dont les clés sont des mots et les valeurs leur
définition.
Ce dictionnaire est déjà créé dans le fichier « Dictionnaire_Mot.txt » du dossier « Exercice_11 »,
il faudra le formater en « dictionnaire » et l'ajouter dans votre code.
"""
import os

# Fonction pour charger le contenu du fichier dans un dictionnaire
def creation_dictionnaire(fichier):
    dictionnaire = {}
    
    # Ouvrir le fichier manuellement
    f = open(fichier, 'r', encoding='utf-8')
    
    # Lire chaque ligne du fichier
    for ligne in f:
        # Séparer le mot et la définition
        mot, definition = ligne.split(" -> ")
        dictionnaire[mot] = definition.replace("\n", "")

        # Vérifier si la définition est vide
        if not definition:
            print("Avertissement : Le mot '" + mot + "' n'a pas de définition.")

    # Fermer le fichier après la lecture
    f.close()
    
    return dictionnaire

# Fonction pour trier le dictionnaire par la longueur des définitions
def trier_par_definition(dictionnaire):
    # Trie les éléments du dictionnaire par la longueur de leurs définitions (valeurs), de la plus longue à la plus courte.
    dictionnaire_trie = sorted(dictionnaire.items(), key=lambda x: len(x[1]), reverse=True)
    
    # Retourner le dictionnaire trié
    return dict(dictionnaire_trie)

# Fonction pour afficher le dictionnaire
def afficher_dictionnaire(dico):
    for mot, definition in dico.items():
        print(mot + " -> " + definition)

# Chemin du fichier
fichier = r"D:\Licence\Lauzero Paul (Python)\Dictionnaire_Mot.txt"

# Vérifier si le fichier existe
if not os.path.exists(fichier):
    print("Erreur : Le fichier " + fichier + " est introuvable.")
else:
    # Charger les données depuis le fichier
    dico = creation_dictionnaire(fichier)

    # Trier les données par la longueur des définitions
    dico_trie = trier_par_definition(dico)

    # Afficher le dictionnaire trié
    if dico_trie:
        afficher_dictionnaire(dico_trie)
    else:
        print("Le dictionnaire est vide.")