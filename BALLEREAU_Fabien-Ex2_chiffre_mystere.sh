#!/bin/bash

# Demande à l'utilisateur de saisir la borne supérieure (par défaut 100)
read -p "Saisissez la borne supérieure [100] : " borne_supp
borne_supp=${borne_supp:-100}  # Utilise 100 comme valeur par défaut si aucune entrée n'est fournie

# Vérifie si la borne supérieure est un nombre positif
if ! [[ "$borne_supp" =~ ^[0-9]+$ ]]; then
    echo "Erreur : la borne supérieure doit être un nombre positif."
    exit 1  # Quitter le script en cas d'erreur
fi

# Génère un nombre aléatoire entre 1 et la borne supérieure
random=$((RANDOM % borne_supp + 1))

choix=-1  # Initialise la variable choix

# Boucle jusqu'à ce que l'utilisateur trouve le nombre aléatoire
while [ "$choix" -ne "$random" ]; do
    # Demande à l'utilisateur de saisir un nombre
    read -p "Saisissez un nombre entre 1 et $borne_supp : " choix

    # Vérifie si le choix est un nombre valide
    if ! [[ "$choix" =~ ^[0-9]+$ ]]; then
        echo "Erreur : vous devez saisir un nombre."
        continue  # Reprend la boucle en cas d'erreur
    elif [ "$choix" -lt 1 ] || [ "$choix" -gt "$borne_supp" ]; then
        echo "Erreur : le nombre doit être compris entre 1 et $borne_supp."
        continue  # Reprend la boucle en cas d'erreur
    fi

    # Compare le choix de l'utilisateur avec le nombre aléatoire
    if [ "$choix" -gt "$random" ]; then
        echo "Le nombre mystère est plus petit que $choix."
    elif [ "$choix" -lt "$random" ]; then
        echo "Le nombre mystère est plus grand que $choix."
    else
        echo "Bravo, le nombre mystère était $random !!"
    fi
done