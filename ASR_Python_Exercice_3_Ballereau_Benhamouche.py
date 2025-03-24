"""
Auteur : Fabien BALLEREAU, Lehna Benhamouche
04/12/2024

Définir une fonction qui attend le rayon d'un disque puis qui affiche son aire.
Rappel : aire du disque = Pi * rayon^2
Dans le programme principal, on entrera le rayon (un float), puis on affichera l'aire
au format suivant, l'aire étant bien sur calculée par appel à la fonction :
L'aire d'un disque de rayon 19.8 est 1231.6299839133426
Pour utiliser pi, importer la valeur pi du module math en tête de votre code :
from math import pi as Pi # on importe pi du module math et on l'appelle Pi

"""
# Importation de la librairie "pi" du module "math"
from math import pi as Pi

# Déclaration de la fonction ; Formule pour calcul de l'air d'un disque
def air_disque(rayon):
    return Pi * rayon ** 2

# Saisi utilisateur ; rayon
rayon = float(input("Entrer l'air du disque : "))

# Appel de la fonction air_disque
resultat = air_disque(rayon)

# Affichage du résultat
print("L'aire d'un disque de rayon", rayon, "est", resultat)