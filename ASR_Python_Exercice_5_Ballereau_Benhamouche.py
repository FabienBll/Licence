"""
Auteur : Fabien BALLEREAU, Lehna BENHAMOUCHE
11/12/2024

Exercice 5
Ecrire un programme qui attend dans cet ordre :
Un capital initial C0
Un taux d'intérêt annuel T. Pour 2%, on attend 0.02.
Un coefficient multiplicateur "coefficient"
Le programme retourne le nombre d'années N nécessaires pour que le
capital soit multiplié par "interet" ainsi que le capital obtenu après ces "annee" années.
Modèle de sortie :
Capital initial : 5231
Taux : 5.0 %
Apres 15 ans, votre capital aura été multiplié par 2
Vous disposerez alors de 10874
"""

# Le programme attend en entrée un capital initial, un taux d'intérêt et un coefficient multiplicateur.
capital = int(input("Capital initial : "))
interet = float(input("Taux d'intérêt : "))
coefficient = int(input("Coefficient multiplicateur : "))

# Calcul du total en utilisant le coefficient afin de savoir quand la boucle devra s'arrêter (donc l'objectif à atteindre)
total = capital * coefficient
gain = capital
annee = 0

# Boucle permettant d'ajouter les intérêts chaque année et vérifie si les gains ont atteint l'objectif souhaité
while gain < total:
    annee += 1
    gain += gain * interet

# Le programme renvoie le nombre d'année nécessaires pour que le capital soit multiplié par le coefficient multiplicateur. 
# Il renvoie aussi le capital obtenu après le nombre d'années. 
# Par exemple : on entre un capital de 5231 et un taux de 0.05 (5%) on attend un retour -> Après 15 ans, votre capital aura été multiplié par 2, vous disposerez alors de 10874.
print("Capital initial :", int(capital))
# L'intérêt est arrondi au dixième car certains calcul peuvent être faussés comme 0.14 * 100 qui donne 14.0000002 et non 14.0
print("Taux :", round(interet*100,1), "%")
print("Après", annee, "ans, votre capital aura été multiplié par",  int(coefficient))
print("Vous disposerez alors de", int(gain))