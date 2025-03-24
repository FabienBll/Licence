#!/bin/bash

# Demande à l'utilisateur de saisir la durée de la micro-sieste en secondes
read -p "Veuillez saisir la durée en secondes pour la micro-sieste : " duree

# Vérifier si la durée est un nombre positif
if [ "$duree" -le 0 ]; then
    echo "Erreur : la durée doit être un nombre positif."
    exit 1  # Quitte le script en cas d'erreur
fi

# Enregistre l'heure de début de la micro-sieste
heure_debut=$(date +"%H:%M:%S")
echo "Il est $heure_debut et la micro-sieste commence..."

# Met en pause pour la durée spécifiée
sleep $duree

# Enregistre l'heure de fin de la micro-sieste
heure_fin=$(date +"%H:%M:%S")
echo "... il est $heure_fin, bon retour parmi nous !"
echo "L'utilisateur $(whoami) a effectué une micro-sieste de ${duree}s entre $heure_debut et $heure_fin"