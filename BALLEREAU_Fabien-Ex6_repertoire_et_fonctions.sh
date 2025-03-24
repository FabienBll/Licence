#!/bin/bash

# Fonction pour analyser le contenu d'un répertoire
analyser_repertoire() {
    local repertoire="$1"
    local compteur_fichiers=0
    local compteur_sous_repertoires=0

    for element in "$repertoire"/*; do
        # Exécuter le script secondaire pour obtenir le type de fichier
        ./BALLEREAU_Fabien-Ex4_le_retour_du_fichier.sh "$element"
        type=$?

        # Utilise la commande case pour traiter les différents types de fichiers
        case "$type" in
            1 | 3) # Fichier ordinaire et entrée spéciale
                ((compteur_fichiers++))
                ;;
            2) # Répertoire
                ((compteur_sous_repertoires++))
                compteur_fichiers=$((compteur_fichiers + $(find "$element" -type f | wc -l)))
                compteur_sous_repertoires=$((compteur_sous_repertoires + $(find "$element" -type d | wc -l) - 1))
                ;;
            *) # Autre cas (inexistant ou inaccessible)
                ;;
        esac
    done

    echo "Il y a $compteur_sous_repertoires sous-répertoires et $compteur_fichiers fichiers dans le répertoire $repertoire"
}

# Vérifie qu'il y ait au moins un paramètre passé
if [ "$#" -ne 1 ]; then
    echo "Erreur : un seul paramètre (répertoire) doit être passé au script."
    exit 1
fi

# Vérifie que le paramètre soit un répertoire existant
if [ ! -d "$1" ]; then
    echo "Erreur : le paramètre passé n'est pas un répertoire existant."
    exit 1
fi

# Appelle la fonction pour analyser le répertoire
analyser_repertoire "$1"