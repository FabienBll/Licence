# Script Creation_Utilisateurs
# BALLEREAU Fabien
# BENHAMOUCHE Lehna

#/#/#/#/#/#/#/#/#/#/#/#/
#/#/#/# Variables #/#/#/
#/#/#/#/#/#/#/#/#/#/#/#/

# Récupérer l'emplacement du script
$Emplacement_Script = $PSScriptRoot

# Chemin du fichier de journalisation
$Emplacement_Log = "$Emplacement_Script/logfile.txt"

# Chemin du fichier CSV
$Fichier_CSV = "$Emplacement_Script/Users.csv"
$Fichier_CSV_Succes = "$Emplacement_Script/Users_Created.csv"
$Fichier_CSV_Echecs = "$Emplacement_Script/Users_Not_Created.csv"

# Importer le contenu du fichier CSV
$Contenu_CSV = Import-Csv -Path $Fichier_CSV

# Initialiser les fichiers de sortie
Out-File -FilePath $Fichier_CSV_Succes -Encoding UTF8
Out-File -FilePath $Fichier_CSV_Echecs -Encoding UTF8

# Écrire les en-têtes des fichiers CSV
$Contenu_CSV | Select-Object -First 0 | Export-Csv -Path $Fichier_CSV_Succes -NoTypeInformation -Force -Encoding UTF8
$Contenu_CSV | Select-Object -First 0 | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Force -Encoding UTF8

#/#/#/#/#/#/#/#/#/#/#/#/
#/#/#/# Fonctions #/#/#/
#/#/#/#/#/#/#/#/#/#/#/#/

# Fonction pour écrire une entrée dans le fichier de journalisation
function Creation_Log {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Message, # Le message à afficher

        [Parameter(Mandatory=$true)]
        [ValidateSet("DEBUT", "INFORMATION", "AVERTISSEMENT", "ERREUR", "FIN")]
        [string]$Level, # Affichage du niveau/status de journalisation

        [Parameter(Mandatory=$true)]
        [string]$LogFile # Chemin du fichier de journalisation
    )

    # Formatage de l'entrée de journal
    $logEntry = "$(Get-Date -Format 'dd-MM-yyyy HH:mm:ss') --- $Level --- $Message"

    # Ajout au fichier de journalisation
    Add-Content -Path $LogFile -Value $logEntry
}

# Fonction pour générer un mot de passe aléatoire
function Generer_Mot_De_Passe {
    # Ensemble de caractères possibles
    $lowercase = 'abcdefghijklmnopqrstuvwxyz'
    $uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    $digits = '0123456789'
    $special = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    # Générer un mot de passe de 10 caractères avec au moins une minuscule, une majuscule, un chiffre et un caractère spécial
    $password = ($lowercase | Get-Random -Count 1) -join ''
    $password += ($uppercase | Get-Random -Count 1) -join ''
    $password += ($digits | Get-Random -Count 1) -join ''
    $password += ($special | Get-Random -Count 1) -join ''
    $password += ($lowercase + $uppercase + $digits + $special | Get-Random -Count 6) -join ''

    # Mélanger les caractères pour éviter un ordre prévisible
    $password = -join ($password.ToCharArray() | Get-Random -Count $password.Length)

    $password = $password.Substring(0, 12)

    return $password
}

# Fonction pour supprimer les Accents d'une chaîne
function Remove-Accents {
    param (
        [string]$Texte_A_Formater
    )

    $Accents = @{
        'à' = 'a'; 'â' = 'a'; 'ä' = 'a'; 'á' = 'a'; 'ã' = 'a'; 'å' = 'a';
        'è' = 'e'; 'ê' = 'e'; 'ë' = 'e'; 'é' = 'e';
        'ì' = 'i'; 'î' = 'i'; 'ï' = 'i'; 'í' = 'i';
        'ò' = 'o'; 'ô' = 'o'; 'ö' = 'o'; 'ó' = 'o'; 'õ' = 'o';
        'ù' = 'u'; 'û' = 'u'; 'ü' = 'u'; 'ú' = 'u';
        'ç' = 'c'; 'ñ' = 'n'
    }

    foreach ($Accent in $Accents.Keys) {
        $Texte_A_Formater = $Texte_A_Formater -replace $Accent, $Accents[$Accent]
    }

    return $Texte_A_Formater
}

#/#/#/#/#/#/#/#/#/#/#/#/
#/#/#/ Exécution /#/#/#/
#/#/#/#/#/#/#/#/#/#/#/#/

# Parcourir chaque utilisateur dans le fichier CSV
foreach ($Utilisateur in $Contenu_CSV) {
    $Nom = $Utilisateur.Nom
    $Prenom = $Utilisateur.Prénom
    $Service = $Utilisateur.Services
    $Mot_De_Passe = $Utilisateur."Mot de passe"
    $User_Name = $Utilisateur.UserName
    $User_Name = Remove-Accents -Texte_A_Formater $User_Name
    $User_Name = $User_Name -replace " ",""

    # Correction de l'affichage du nom complet
    $Display_Name = $Nom.ToUpper() + " " + $Prenom

    Creation_Log -Message "======== $Prenom $Nom ========" -Level "INFORMATION" -LogFile $Emplacement_Log

    if ([string]::IsNullOrEmpty($Service)) {
        $Service = "People"
    }

    # Vérification de la présence d'un utilisateur
    $Verif_Presence_Utilisateur = Get-ADUser -Filter {GivenName -eq $Prenom -and Surname -eq $Nom -and Department -eq $Service} -ErrorAction SilentlyContinue

    try {
        # Si aucun compte n'a été trouvé, le script continu
        if (-not $Verif_Presence_Utilisateur) {
            Creation_Log -Message "Aucun compte trouvé pour $Display_Name" -Level "INFORMATION" -LogFile $Emplacement_Log
        # Si un compte a été trouvé on vérifie si l'employé à déjà un UserName
        } elseif ($User_Name) {
            # Vérification de la présence d'un utilisateur avec le même UserName
            $Verif_Presence_UserName = Get-ADUser -Filter {SamAccountName -eq $User_Name} -ErrorAction SilentlyContinue

            # Si aucun compte n'a été trouvé le script continu
            if (-not $Verif_Presence_UserName) {
                Creation_Log -Message "Un compte avec le nom $Display_Name a été trouvé mais pas avec le UserName $User_Name" -Level "INFORMATION" -LogFile $Emplacement_Log
            
            # Sinon le script passe à l'employé suivant
            } else {
                Creation_Log -Message "Un compte existe déjà pour $User_Name." -Level "AVERTISSEMENT" -LogFile $Emplacement_Log
                $Utilisateur | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Append -Encoding UTF8
                continue            
            }
        # Si un compte a été trouvé et que l'employé n'a pas de UserName le script passe à l'employé suivant.
        } else {
            Creation_Log -Message "Un compte existe déjà pour $Display_Name." -Level "AVERTISSEMENT" -LogFile $Emplacement_Log
            $Utilisateur | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Append -Encoding UTF8
            continue
        }
    } catch {
        Creation_Log -Message "Erreur lors de la vérification de l'utilisateur $Display_Name : $_" -Level "ERREUR" -LogFile $Emplacement_Log
        $Utilisateur | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Append -Encoding UTF8
        continue
    }

    # Vérifier si le nom d'utilisateur est vide
    if ([string]::IsNullOrEmpty($User_Name)) {
        $User_Name = $Prenom.Substring(0, 1).ToLower() + $Nom.ToLower()
        $User_Name = $User_Name -replace " ", ""

        # Vérifier si le nom d'utilisateur est déjà utilisé
        $Verif_Presence_Utilisateur = Get-ADUser -Filter {SamAccountName -eq $User_Name} -ErrorAction SilentlyContinue
        if ($Verif_Presence_Utilisateur) {
            Creation_Log -Message "Nom d'utilisateur $User_Name déjà utilisé. Modification requise." -Level "AVERTISSEMENT" -LogFile $Emplacement_Log
            $User_Name = $Prenom.ToLower() + "." + $Nom.ToLower()
            $User_Name = $User_Name -replace " ", ""

            $Verif_Presence_Utilisateur = Get-ADUser -Filter {SamAccountName -eq $User_Name} -ErrorAction SilentlyContinue
            if ($Verif_Presence_Utilisateur) {
                Creation_Log -Message "Le nouveau nom d'utilisateur $User_Name est également déjà utilisé !" -Level "ERREUR" -LogFile $Emplacement_Log
                Creation_Log -Message "Le compte de $Display_Name n'a pas pu être créé !" -Level "ERREUR" -LogFile $Emplacement_Log
                $Utilisateur | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Append -Encoding UTF8
                continue
            }            
        }
    }

    # Vérification et génération du mot de passe si nécessaire
    if ([string]::IsNullOrEmpty($Mot_De_Passe)) {
        Creation_Log -Message "Aucun mot de passe trouvé pour $Display_Name. Un nouveau sera généré." -Level "INFORMATION" -LogFile $Emplacement_Log
        $Mot_De_Passe = Generer_Mot_De_Passe
    }

    # Attribution de l'UO en fonction du service
    switch ($Service) {
        "Comptabilité" {$UO = "OU=Comptabilite,OU=Services,DC=upec,DC=local"}
        "IT" {$UO = "OU=IT,OU=Services,DC=upec,DC=local"}
        "Direction" {$UO = "OU=Direction,OU=Services,DC=upec,DC=local"}
        "Externe" {$UO = "OU=Externe,OU=Services,DC=upec,DC=local"}
        "People" {$UO = "OU=People,OU=Services,DC=upec,DC=local"}
    }

    Creation_Log -Message "UO assignée à l'utilisateur : $UO" -Level "INFORMATION" -LogFile $Emplacement_Log

    # Vérification de l'existence du compte avant la création
    $Verif_Presence_Utilisateur = Get-ADUser -Filter {SamAccountName -eq $User_Name} -ErrorAction SilentlyContinue
    if ($Verif_Presence_Utilisateur) {
        Creation_Log -Message "Le compte $User_Name existe déjà." -Level "AVERTISSEMENT" -LogFile $Emplacement_Log
        $Utilisateur | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Append -Encoding UTF8
        continue
    }

    # Création de l'utilisateur
    New-ADUser -SamAccountName $User_Name `
                -UserPrincipalName $User_Name `
                -GivenName $Prenom `
                -Surname $Nom `
                -Name $Display_Name `
                -Description $Service `
                -Department $Service `
                -Path $UO `
                -AccountPassword (ConvertTo-SecureString -AsPlainText $Mot_De_Passe -Force) `
                -Enabled $true

    # Vérification de la création du compte
    $Verif_Presence_Utilisateur = Get-ADUser -Filter {SamAccountName -eq $User_Name} -ErrorAction SilentlyContinue

    if ($Verif_Presence_Utilisateur) {
        Creation_Log -Message "Utilisateur $User_Name créé avec succès !" -Level "INFORMATION" -LogFile $Emplacement_Log
        "$User_Name,$Display_Name,$Mot_De_Passe" | Out-File -FilePath $Fichier_CSV_Succes -Append -Encoding UTF8
    } else {
        Creation_Log -Message "Erreur lors de la création du compte $User_Name pour $Display_Name." -Level "ERREUR" -LogFile $Emplacement_Log
        $Utilisateur | Export-Csv -Path $Fichier_CSV_Echecs -NoTypeInformation -Append -Encoding UTF8
    }
}