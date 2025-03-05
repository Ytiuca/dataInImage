# dataInImage

## Encoding/decoding

Ce projet permet de générer des images multicolores à base de textes, ce qui permet de "cacher" des messages sous forme d'images.

![image](https://github.com/user-attachments/assets/8a78c261-0155-42ab-a427-a1efd3fb4f77)

Cette image correspond par exemple au livre "alice au pays des merveilles".

Ce projet permet aussi de récupérer le message caché dans une image.

## BG_Changing

Ce projet permet de générer des fonds d'écran aléatoires qui changent selon un interval donné.
Il faut dans les paramètres windows que la section *Personnaliser votre arrière-plan* soit sur *Image*.
Je recommande que la section *Choisir un ajustement pour votre image de bureau* soit sur *Étirer* bien que vous pouvez l'ajuster selon vos goûts.
![image paramétrage windows](image.png)

### Setup

- créer un .env
- ajouter la variable "BG_PATH" et indiquer le chemin ou sera généré le background

Vous pouvez ajouter les variables `X_LENGTH`, `Y_LENGTH` et `TIME_BEFORE_BG_CHANGE` afin que le programme puisse être exécuté automatiquement au démarrage.

Il vous faudra aussi ajouter le fichier *"startup.lnk* dans le dossier de démarrage de windows.

Appuyer sur *Win+r* puis entrez *shell:startup* et coller le fichier dedans.

Vous pouvez aussi ajouter les variables `SAVE_BG` et `SAVE_DIRECTORY` afin d'enregistrer les fonds d'écran générés.

```.env
BG_PATH=C:\path\to\generated\background
X_LENGTH=*optionnal*
Y_LENGTH=*optionnal*
TIME_BEFORE_BG_CHANGE=*optionnal*
SAVE_BG=*optionnal* true|false
SAVE_DIRECTORY=C:\path\to\saved\folder
```

Il est possible de lancer le programme avec des arguments:

`python main.py -x INT -y INT -d INT -s OPTIONNAL`

où
-x, --x-length est un entier représentant le nombre de pixel sur l'axe x
-y, --y-length est un entier représentant le nombre de pixel sur l'axe y
-d, --delay est un entier représentant le temps entre chaque changement de fond d'écran (0 pour aucun)
-s, --save est un flag optionnel, s'il est présent les fond d'écrans seront enregistrés dans le `SAVE_DIRECTORY`
