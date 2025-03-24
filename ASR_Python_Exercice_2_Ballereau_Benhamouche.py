"""
Auteur : Fabien BALLEREAU, Lehna Benhamouche
04/12/2024

Un organisme de location de voitures propose à ses clients 2 tarifs :
tarif essence :
location : 40 Euros / jour
kilométrage : 15 cts / km
tarif diesel :
location : 50 Euros / jour
kilométrage : 10 cts / km
On entrera dans cet ordre la distance à parcourir et la durée de la location. Ce sont deux entiers.
Puis le programme produira un état de sortie détaillé indiquant le meilleur choix, au format suivant :
Pour 10 jours et 1540 km
avec un véhicule à essence : 631.0
avec un véhicule diesel : 654.0
Véhicule à essence conseillé
"""
# Saisie utilisateur : Distance, Durée
distance = int(input("Distance à parcourir : "))
duree_location = int(input("Durée de la location : "))

# Affichage Durée et Distance saisies
print("Pour", duree_location, "jours et", distance, "km")

# Déclaration et calcule des variables + arrondie au dixième près
essence = round(40 * duree_location + 0.15 * distance, 1)
diesel = round(50 * duree_location + 0.10 * distance, 1)

# Affichage des résultats des calculs
print("avec un véhicule à essence :", essence)
print("avec un véhicule diesel :", diesel)

# Affichage du meilleur choix conseillé
if essence < diesel:
    print("Véhicule à essence conseillé")
elif essence > diesel:
    print("Véhicule diesel conseillé")
else:
    print("Véhicule diesel et essence au même prix")