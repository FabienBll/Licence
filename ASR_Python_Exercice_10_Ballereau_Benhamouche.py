"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
11/12/2024

Chercher dans tous les fichiers d'un dossier donné (Exercice_10) ceux qui contiennent des lignes commençant par un mot donné et écrire dans un
fichier rapport la liste des fichiers répondant au critère.
Le rapport sera présenté de la façon suivante :
Date :
Dossier :
fichier1
ligne du fichier1 commençant par le mot cherché
ligne suivante du fichier1 commençant par le mot cherché
...
dernière ligne du fichier1 commençant par le mot cherché
fichier2
ligne du fichier2 commençant par le mot cherché
ligne suivante du fichier2 commençant par le mot cherché
...
dernière ligne du fichier2 commençant par le mot cherché
etc
"""

import os
from datetime import datetime

# Déclaration fonction "obtenir_date_actuelle", renvoie la date actuelle sous forme de chaîne de caractères
def obtenir_date_actuelle():
    return "Date : " + str(datetime.now()) + "\n"

# Déclaration fonction "chercher_lignes", prend en entrée : dossier, mot
# Recherche les fichiers dans le dossier contenant des lignes qui commencent par le mot donné
def chercher_lignes(dossier, mot):
    
    # Initialise un dictionnaire pour stocker les résultats
    resultat = {}

    # Parcours les fichiers du dossier
    for fichier in os.listdir(dossier):
        chemin = os.path.join(dossier, fichier)

        # Vérifie si l'élément est un fichier
        if os.path.isfile(chemin):
            # Ouvre le fichier en mode lecture avec encodage UTF-8
            f = open(chemin, "r", encoding="utf-8")
            lignes = []
            # Parcours chaque ligne du fichier
            for ligne in f:
                if ligne.lower().startswith(mot.lower()): 
                    # Ajoute la ligne à la liste si elle commence par le mot recherché
                    lignes.append(ligne.strip())
            # Ferme le fichier après lecture
            f.close()
            # Si des lignes correspondant au critère ont été trouvées
            if lignes:
                # Ajoute le fichier et ses lignes trouvées au dictionnaire
                resultat[fichier] = lignes
    return resultat

# Déclaration fonction "ecrire_rapport", prend en entrée : resultat, dossier
# Écrit un rapport des résultats dans un fichier "rapport.txt"
def ecrire_rapport(resultat, dossier):

    # Ouvre (ou crée) un fichier rapport.txt avec les droits d'écriture et encodage UTF-8
    rapport = open(os.path.join(dossier, "rapport.txt"), "w", encoding="utf-8")
    # Écrit la date actuelle dans le rapport
    rapport.write(obtenir_date_actuelle())
    # Écrit le nom du dossier dans le rapport
    rapport.write("Dossier : " + dossier + "\n\n")

    # Parcours les fichiers et les lignes trouvées dans les résultats
    for fichier, lignes in resultat.items():
        # Écrit le nom du fichier
        rapport.write(fichier + "\n")
        for ligne in lignes:
            # Écrit chaque ligne correspondant au critère
            rapport.write(ligne + "\n")
        # Ajoute un espace entre les fichiers dans le rapport
        rapport.write("\n")
    # Ferme le fichier de rapport
    rapport.close()

# Demande à l'utilisateur d'entrer un mot à rechercher dans les fichiers
mot = input("Entrez un mot : ")

# Déclare le dossier contenant les fichiers à traiter
dossier = "Exercice_10"

# Appelle la fonction "chercher_lignes" pour rechercher les fichiers qui correspondent aux critères
resultat = chercher_lignes(dossier, mot)

# Si des résultats ont été trouvés, crée le rapport
if resultat:
    # Appelle la fonction "ecrire_rapport" pour générer le fichier de rapport
    ecrire_rapport(resultat, dossier)
    print('Rapport nommé "rapport.txt" créé dans le dossier Exercice_10.')
else:
    print("Aucun fichier contenant des lignes commençant par", mot, "n'a été trouvé.")