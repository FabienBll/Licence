"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
08/01/2025

Exercice 12
Exercice portant sur l'utilisation basique des expressions régulières
Objectifs : comprendre les notions fondamentales relatives à l'utilisation des expressions régulières.

Le script doit récupérer le contenu d'un fichier, puis il doit répondre à plusieurs consignes consistant à utiliser regex afin de rassembler des motifs précis comme
le regex [A-Z0-9] qui affiche toutes les lignes contenant des chiffres ou des majuscules.
"""

import re, os

# Fonction pour afficher le titre de chaque section dans le fichier de sortie
def afficheTitre(titre, fichier_sortie):
    fichier_sortie.write('\n' + '*' * len(titre) + '\n')
    fichier_sortie.write(f'{titre}\n')
    fichier_sortie.write('*' * len(titre) + '\n')

# Fonction pour afficher les lignes qui correspondent à une expression régulière dans le fichier de sortie
def afficheLignes(regexp, lignes, fichier_sortie):
    matching_lines = [ligne for ligne in lignes if re.search(regexp, ligne)]
    for line in matching_lines:
        fichier_sortie.write(line)
    fichier_sortie.write(f'***** {len(matching_lines)} lignes trouvees *****\n')

# Vérification de l'existence du fichier
if not os.path.exists("RegExp_Exercice_12.txt"):
    print("Erreur : Le fichier RegExp_Exercice_12.txt n'existe pas.")
else:
    # Charger le fichier d'entrée avec l'encodage windows-1252
    with open("RegExp_Exercice_12.txt", "r", encoding="windows-1252") as fichier_entree:
        lignes = fichier_entree.readlines()

    # Ouvrir le fichier de sortie avec l'encodage windows-1252 pour écrire
    with open("SortieRegExp_Exercice_12.txt", "w", encoding="windows-1252") as fichier_sortie:

        # En-tête du fichier de sortie
        fichier_sortie.write("*************************************************" + '\n')
        fichier_sortie.write("PYTHON : Fichier de sortie de l\'exercice 2 du TP4" + '\n')
        fichier_sortie.write("*************************************************" + '\n')

        # Lignes contenant au moins un chiffre ou une majuscule
        afficheTitre("1.a : lignes contenant des chiffres ou des majuscules", fichier_sortie)
        afficheLignes(r'[A-Z0-9]', lignes, fichier_sortie)

        # Lignes contenant au moins un point
        afficheTitre("1.b : lignes contenant des points", fichier_sortie)
        afficheLignes(r'\.', lignes, fichier_sortie)

        # Lignes contenant exactement trois points consécutifs
        afficheTitre("1.c : lignes contenant trois points (...) ", fichier_sortie)
        afficheLignes(r'\.\.\.', lignes, fichier_sortie)

        # Lignes avec nombres hexadécimaux entourés de blancs
        afficheTitre("1.d : lignes contenant des nombres hexadecimaux separes par des blancs", fichier_sortie)
        afficheLignes(r'(^|\s)[0-9a-fA-F]+(\s|$)', lignes, fichier_sortie)

        # Lignes avec un mot d'au moins 12 caractères alphanumériques
        afficheTitre("1.e : lignes contenant un mot d'au moins 12 caracteres alphanumeriques", fichier_sortie)
        afficheLignes(r'\b[a-z0-9]{12,}\b', lignes, fichier_sortie)

        # Lignes contenant exactement 5 lettres 'a'
        afficheTitre("1.f : lignes contenant exactement 5 lettres a (pas nécessairement successives)", fichier_sortie)
        afficheLignes(r'^(?=(?:[^a]*a){5}[^a]*$).{1,}$', lignes, fichier_sortie)

        # Lignes contenant au moins un crochet ([ ou ])
        afficheTitre("1.g : lignes contenant des crochets ( ] ou [ )", fichier_sortie)
        afficheLignes(r'[\[\]]', lignes, fichier_sortie)

        # Lignes avec uniquement des lettres 'a' et des espaces
        afficheTitre("1.h : lignes ne contenant que des lettres a et des espaces", fichier_sortie)
        afficheLignes(r'^[a ]+$', lignes, fichier_sortie)

        # Lignes ressemblant à une adresse IP (quatre groupes de 1-3 chiffres séparés par des points)
        afficheTitre("1.i : lignes contenant quelque chose qui ressemble a une adresse IP", fichier_sortie)
        afficheLignes(r'(\d{1,3}\.){3}\d{1,3}', lignes, fichier_sortie)

        # Lignes complètement vides (uniquement un saut de ligne)
        afficheTitre("2.a : lignes vides", fichier_sortie)
        afficheLignes(r'^\n$', lignes, fichier_sortie)

        # Lignes blanches contenant uniquement des espaces
        afficheTitre("2.b : lignes blanches", fichier_sortie)
        afficheLignes(r'^\s+\n$', lignes, fichier_sortie)

        # Lignes non vides (au moins un caractère)
        afficheTitre("2.c : lignes non vides", fichier_sortie)
        afficheLignes(r'.+', lignes, fichier_sortie)

        # Lignes ne contenant pas la lettre 'a'
        afficheTitre("3.a : lignes qui ne contiennent pas de a", fichier_sortie)
        afficheLignes(r'^[^a]*$', lignes, fichier_sortie)

        # Lignes sans espaces
        afficheTitre("3.b : lignes qui ne contiennent pas des espaces", fichier_sortie)
        afficheLignes(r'^[^\s]*$', lignes, fichier_sortie)

        # Lignes sans chiffres décimaux
        afficheTitre("3.c : lignes qui ne contiennent pas des chiffres décimaux", fichier_sortie)
        afficheLignes(r'^[^\d]*$', lignes, fichier_sortie)

        # Lignes commençant par un numéro de téléphone (01 64 25 89 78)
        afficheTitre("4 : lignes qui débutent par un numéro de téléphone au format 01 23 45 67 89", fichier_sortie)
        afficheLignes(r'^(\d{2}\s){4}\d{2}.*$', lignes, fichier_sortie)

        # Lignes commençant par un téléphone avec ., - ou espace comme séparateurs
        afficheTitre("5 : idem 4 mais on peut avoir . ou - a la place des espaces", fichier_sortie)
        afficheLignes(r'^(\d{2}([^\w\d])?){4}\d{2}.*$', lignes, fichier_sortie)

        # Téléphone débutant par '0', ce dernier entouré ou non de parenthèses
        afficheTitre("6 : idem 5 mais le 0 peut être entoure de parentheses", fichier_sortie)
        afficheLignes(r'^\(?0\)?\d([^\w\d])?\d{2}([^\w\d])?\d{2}([^\w\d])?\d{2}([^\w\d])?\d{2}.*$', lignes, fichier_sortie)

        # Lignes finissant par un numéro de téléphone avec séparateurs variés
        afficheTitre("7 : terminent par un tel au format 0 123 456 789, espaces, - ou . et (0)", fichier_sortie)
        afficheLignes(r'.*\(?0\)?([^\w\d])?\d{3}([^\w\d])?\d{3}([^\w\d])?\d{3}$', lignes, fichier_sortie)


    if os.path.getsize("SortieRegExp_Exercice_12.txt") == 0: 
        print("Le fichier SortieRegExp_Exercice_12.txt est vide.")