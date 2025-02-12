# Manuel d'utilisation

## Introduction

Le script `script.py` permet de vérifier si des mots de passe utilisateur ont été compromis en utilisant l'API "Have I Been Pwned" (HIBP). Il se base sur le site HIBP pour effectuer ces vérifications et affiche les résultats dans une interface graphique construite avec Tkinter.

## Prérequis

1. Une machine avec Python 3.x installé.
2. Un fichier de configuration nommé `config.ini` avec les sections et format requis.
3. Un fichier de base de données CSV contenant les colonnes `login` et `password` (hash SHA-1 du mot de passe).
4. Les bibliothèques Python suivantes doivent être installées :
   - `requests`
   - `tkinter`

## Fichier de base

Description des sections du fichier **config.ini** :

[api]
url = https://api.pwnedpasswords.com/range

## Lancer l'outil

### Exécution du script avec l'interface graphique

1. Préparer le fichier de configuration et le fichier de base de données :
    - Créer le fichier `config.ini` avec le contenu ci-dessus.
    - Préparer un fichier de base de données CSV avec les colonnes `login` et `password` (hash SHA-1 du mot de passe) :
      ```csv
      login;password
      user1;5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
      user2;0ef76e1bc1339a927d8929d27aa432e5c26f4e2f
      ```
2. Exécuter la commande suivante dans le terminal pour lancer le script :
    ```bash
    python scriptv3_interface_graphique.py
    ```
3. Utiliser l'interface graphique :
    - Une fenêtre Tkinter s'ouvrira.
    - Sélectionnez le fichier de configuration et le fichier de base de données en cliquant sur les boutons "Parcourir".
    - Cliquez sur le bouton "Exécuter" pour lancer la vérification des mots de passe.
    - Les résultats s'afficheront dans la zone de texte située en bas de l'interface.

### Utilisation de la surcharge via les paramètres de ligne de commande

Vous pouvez également fournir des chemins de fichiers ou une URL d'API directement via les paramètres de ligne de commande pour surcharger les valeurs dans le fichier de configuration.

Arguments de ligne de commande disponibles :
- `--config` : Chemin vers le fichier de configuration.
- `--db` : Chemin vers le fichier de base de données.
- `--api_url` : URL de l'API HIBP à utiliser.

#### Exemples

**Fournir un fichier de configuration et un fichier de base de données**

Exécutez la commande suivante pour spécifier les fichiers à utiliser :
      ```bash
      python scriptv3_interface_graphique.py --config chemin/vers/config.ini --db chemin/vers/bdd.csv
      ```
**Surcharger l'URL de l'API**

Exécutez la commande suivante pour spécifier une nouvelle URL d'API :
      ```bash
      python scriptv3_interface_graphique.py --config chemin/vers/config.ini --db chemin/vers/bdd.csv --api_url https://nouvelle-api.com/range
      ```
**Utiliser uniquement l'URL de l'API en surchargeant la configuration**

Exécutez la commande suivante pour uniquement surcharger l'URL de l'API :
      ```bash
      python scriptv3_interface_graphique.py --api_url https://nouvelle-api.com/range
      ```

Vous devriez maintenant pouvoir copier ce texte dans un fichier `.md`. Si vous avez besoin d'autres modifications ou si quelque chose ne fonctionne pas comme prévu, n'hésitez pas à me le faire savoir.
