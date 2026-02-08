# Guide d'utilisation — Creality K1C (imprimante du club)

## 0. Préambule

Cette documentation décrit l'utilisation de l'imprimante 3D Creality K1C disponible au club.

- **Buse (nozzle)** : 0.4 mm (buse d'origine)
- **Matériaux compatibles** : PLA, PETG, ABS (en pratique nous utilisons principalement du PLA)
- **Fil principal utilisé au club** : PLA Overture Matte

Remarque importante : bien qu'il soit théoriquement possible d'imprimer des filaments chargés (par ex. fibres de carbone), la buse d'origine de notre machine n'est pas appropriée pour ces matériaux abrasifs et nous ne recommandons pas leur utilisation avec l'équipement actuel.

## 1. Mise en route

### a. Mise sous tension

- Mettre la machine sous tension avec l'interrupteur arrière.

### b. Chargement du filament

- Découper proprement l'extrémité du fil (biseaux à 45° utiles).
- Insérer le filament dans l'orifice d'entrée jusqu'à sentir qu'il descend d'environ 1 cm à l'intérieur de la tête.
- Bloquer le maintien du filament au niveau de la tête (verrouillage du tendeur).

### c. Test d'extrusion

- Effectuer une extrusion manuelle depuis l'écran pour vérifier que le filament sort correctement.

> Une calibration de base a déjà été réalisée sur cette machine. Toutefois, si la première couche est mauvaise ou si l'imprimante a été déplacée, il faut relancer la procédure de calibration complète depuis l'écran avant d'imprimer.

## 2. Impressions

### a. Préparation du G-code (sur PC)

Deux options disponibles sur le PC du club : **Orca Slicer** ou **Creality Print**. Nous recommandons `Orca Slicer` (plus complet), mais `Creality Print` fonctionne aussi.

#### Exemple (Orca Slicer) :
- Choisir le profil d'imprimante : **Creality K1C**
- Choisir le profil de filament correspondant (par ex. **PLA Overture Matte**)
- Dans l'onglet « Préparer », importer le fichier 3D (`.stl`).
- Si besoin, modifier les paramètres d'impression : nous recommandons un remplissage (`infill`) de **10–15%** pour la plupart des pièces non structurales.
- Lancer le découpage (slicing) puis exporter le fichier G-code.
- Copier le G-code à la racine de la clé USB (la clé doit ensuite être branchée à la machine).

> Vous pouvez tout à fait préparer le G-code chez vous ; le PC du club est disponible si vous avez besoin d’un poste équipé.

### b. Impression depuis la machine

- Insérer la clé USB contenant le G-code dans la machine.
- Depuis l'écran, cliquer sur l'icône « Accueil » (maison).
- Aller dans l'onglet « Lecteur USB ».
- Sélectionner votre modèle dans la liste.
- Si c'est la première impression depuis longtemps ou la première de la soirée, laisser la case « calibration » cochée (procédure automatique de calibration). Sinon, la décocher pour gagner du temps.
- Cliquer sur « Imprimer » pour lancer l'impression.

Vérifier l'adhésion de la première couche dans les premières minutes. Si la première couche se décolle :

- Arrêter l'impression.
- Vérifier l'état de la surface du plateau ; si nécessaire nettoyer avec une lingette et de l'eau savonneuse, puis bien sécher.
- Relancer une calibration complète avant de réessayer.

### c. Récupération de la pièce

Félicitations, vous devriez avoir votre pièce imprimée :

- Retirer la plaque magnétique du plateau.
- Laisser refroidir légèrement la plaque et la pièce (quelques secondes).
- Plier/tordre doucement la plaque pour décoller l'objet.
- Si nécessaire, finir le dégagement avec la spatule fournie.
- Remettre la plaque en place en alignant les encoches triangulaires avec les points magnétiques.

## 3. Arrêt de la machine

### a. Retirer le filament

- Depuis l'écran, faire une rétraction manuelle (prévoir chauffe si nécessaire) et retirer le filament.
- Déverrouiller le maintien du filament au niveau de la tête avant de tirer le filament depuis la bobine.

### b. Stockage du filament

- Stocker la bobine dans un sachet anti-humidité avec un absorbeur (silica gel).
- Bien scotcher/fermer le sachet pour limiter l'humidité ; sinon le filament peut devenir cassant.

### c. Mise hors tension

- Attendre que la machine ait suffisamment redescendu en température.
- Mettre hors tension le bouton situé à l'arrière.

