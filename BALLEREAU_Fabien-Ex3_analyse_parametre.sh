#!/bin/bash

# Paramètres par défaut
extension=".save"  # Extension par défaut pour les fichiers sauvegardés
mode_verbose=0     # Mode bavard désactivé par défaut

# Lire et gérer les paramètres de la ligne de commande
while [[ $# -gt 0 ]]; do
    case $1 in
        -e|--extension)
            shift
            extension="$1"  # Modifier l'extension par défaut
            ;;
        -v|--verbose)
            mode_verbose=1  # Activer le mode bavard
            ;;
        *)
            # Concaténer les noms de fichiers
            fichiers="$fichiers $1"  # Ajouter le fichier à la liste
            ;;
    esac
    shift  # Passer au paramètre suivant
done

# Isoler les noms des fichiers dans les paramètres de position
set -- $fichiers

# Parcourir la liste des fichiers et faire une copie de sauvegarde
for fichier in "$@"; do
    if [ -f "$fichier" ]; then  # Vérifier si le fichier existe
        cp "$fichier" "${fichier}${extension}"  # Faire une copie de sauvegarde du fichier
        if [ $mode_verbose -eq 1 ]; then  # Si le mode bavard est activé
            echo "Sauvegarde de $fichier en ${fichier}${extension}"  # Informer l'utilisateur
        fi
    else
        if [ $mode_verbose -eq 1 ]; then  # Si le mode bavard est activé
            echo "Le fichier $fichier n'existe pas."  # Informer l'utilisateur que le fichier n'existe pas
        fi
    fi
done