#!/bin/bash

# Vérifie s'il y a bien un seul argument
if [ "$#" -ne 1 ]; then
    exit 0
fi

# Vérification du type de l'argument
if [ -f "$1" ]; then
    exit 1
elif [ -d "$1" ]; then
    exit 2
elif [ -e "$1" ]; then
    exit 3
else
    exit 0
fi