#!/bin/bash

# Demande à l'utilisateur de saisir une série de notes avec un prompt
echo ""
read -p "Saisir un tableau d'entiers : " -a notes
echo ""

# Fonction pour trier un tableau via un "tri par sélection"
tri_par_selection() {
    local -n tableau=$1
    local taille=${#tableau[@]}

    for ((indice = 0; indice < taille-1; indice++)); do
        indice_minimum=$indice
        for ((indice_suivant = indice+1; indice_suivant < taille; indice_suivant++)); do
            if (( tableau[indice_suivant] < tableau[indice_minimum] )); then
                indice_minimum=$indice_suivant
            fi
        done
        # Permute les valeurs
        temp=${tableau[indice]}
        tableau[indice]=${tableau[indice_minimum]}
        tableau[indice_minimum]=$temp
    done
}

# Trier les notes
tri_par_selection notes

# Récupère la note la plus haute et la note la plus basse
note_minimale=${notes[0]}
note_maximale=${notes[-1]}

# Affiche la note la plus basse et la note la plus haute
echo -e "Note minimale : $note_minimale \n"
echo -e "Note maximale : $note_maximale \n"