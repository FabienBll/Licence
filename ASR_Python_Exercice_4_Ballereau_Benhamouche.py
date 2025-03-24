"""
Auteur : Fabien BALLEREAU, Lehna Benhamouche
04/12/2024

Définir une fonction qui attend un caractère et deux nombres entiers C et hauteur, puis qui dessine le
rectangle vide de hauteur lignes et C colonnes dessiné avec le caractère donné.
Par exemple, si le caractère est *, que hauteur = 5 et C = 6, la fonction dessine :
******
*    *
*    *
*    *
******
Dans le programme principal, on entrera dans cet ordre le caractère, le nombre de lignes et le nombre
de colonnes puis on affichauteurera le rectangle vide par appel à la fonction.

"""

# Déclaration fonction "rectangle", prend en entrée : caractr, hauteur, largeur
def rectangle(caractr, hauteur, largeur): 
    """
    La fonction permet de dessiner un rectangle vide en utilisant un caractère donné par l'utilisateur. 
    Par exemple, avec le caractère *, une hauteur de 5 et une largeur de 6, 
    la fonction dessine un rectangle de 5 lignes et 6 colonnes avec des bords en * et un intérieur vide.
    """

    # Affiche le caractère choisi autant de fois que la largeur spécifiée
    ligne_horizontale = caractr * largeur

    # Vérifie si la largeur saisie est 1 (cas particulier pour une colonne unique)
    if largeur == 1:
        # Si la largeur est 1, la ligne verticale est simplement le caractère répété
        ligne_vide = caractr
    else:
        # Sinon, crée une ligne verticale avec le caractère aux extrémités et des espaces au milieu
        ligne_vide = caractr + ' ' * (largeur - 2) + caractr

    # Vérifie si la hauteur saisie est 1 (cas particulier pour une ligne unique)
    if hauteur == 1:
        # Si la hauteur est 1, le rectangle est simplement la ligne horizontale
        rectangle = ligne_horizontale
    else:
        # Sinon, crée le rectangle avec la ligne horizontale en haut et en bas, et les lignes verticales au milieu
        rectangle = ligne_horizontale + '\n' + (ligne_vide + '\n') * (hauteur - 2) + ligne_horizontale
    
    # Retourne le rectangle formé
    return rectangle


# Saisi de l'utilisateur d'entrer le caractère pour dessiner le rectangle
caractr = input("Entrez le caractère : ")
# Saisi de l'utilisateur d'entrer le nombre de lignes (hauteur) du rectangle
hauteur = int(input("Entrez le nombre de lignes : "))
# Saisi de l'utilisateur d'entrer le nombre de colonnes (largeur) du rectangle
largeur = int(input("Entrez le nombre de colonnes : "))

# Affiche le rectangle dessiné en appelant la fonction rectangle avec les paramètres fournis par l'utilisateur
print(rectangle(caractr, hauteur, largeur))