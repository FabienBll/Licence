#!/bin/bash

# Variables
repertoire="./log"
compteur_fichiers_log=0
erreurs_totales=0
avertissements_totaux=0
compteur_fichiers_correspondants=0
compteur_fichiers_totaux=0

# Date du jour
date_du_jour=$(date +%Y%m%d)

# Parcourir les fichiers dans le répertoire
for fichier in "$repertoire"/*; do
    ((compteur_fichiers_totaux++))
    nom_fichier=$(basename "$fichier")
    
    # Extraction de la date et de l'extension
    date_fichier=${nom_fichier:0:8}
    extension_fichier=${nom_fichier##*.}

    if [[ "$date_fichier" == "$date_du_jour" && "$extension_fichier" == "log" ]]; then
        ((compteur_fichiers_correspondants++))
        erreurs=$(grep -c 'ERROR' "$fichier")
        avertissements=$(grep -c 'WARNING' "$fichier")
        echo -e "$nom_fichier \n"
        echo -e "-- ERROR > $erreurs \n"
        echo -e "-- WARNING > $avertissements \n"
        ((erreurs_totales+=erreurs))
        ((avertissements_totaux+=avertissements))
    fi
done

# Afficher les statistiques
echo -e "Nombre de fichiers de log du jour : $compteur_fichiers_correspondants \n"
echo -e "Nombre de fichiers dans le répertoire : $compteur_fichiers_totaux \n"
echo -e "Nombre d'autres fichiers : $((compteur_fichiers_totaux - compteur_fichiers_correspondants)) \n"
echo -e "Nombre total d'erreurs : $erreurs_totales \n"
echo "Nombre total d'avertissements : $avertissements_totaux"