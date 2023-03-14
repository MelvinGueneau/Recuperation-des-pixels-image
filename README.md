# Recuperation-des-pixels-image


Programme de récupération de couleurs d'image
Ce programme Python récupère les différentes couleurs d'une image et les stocke dans un dictionnaire Python. Il utilise la bibliothèque Python "Pillow" pour charger l'image et extraire les données de pixel.

Prérequis
Python 3.x
Pillow (installation avec pip : pip install pillow)
Utilisation
Clonez le dépôt ou téléchargez le fichier color_extractor.py.
Ouvrez une invite de commande dans le répertoire où se trouve le fichier color_extractor.py.
Exécutez la commande suivante : python color_extractor.py <chemin_vers_l'image>
Exemple d'utilisation : python color_extractor.py my_image.png

Le programme va afficher le dictionnaire contenant les couleurs et leur nombre d'occurrences dans l'image.

Fonctionnement
Le programme utilise la méthode getcolors() de la classe Image de la bibliothèque Pillow pour extraire toutes les couleurs de l'image. Les données sont stockées dans une liste de tuples (nombre d'occurrences, couleur) qui est triée en fonction du nombre d'occurrences. Enfin, les données sont stockées dans un dictionnaire où chaque clé est une couleur et chaque valeur est le nombre d'occurrences de cette couleur dans l'image.

Limitations
Le programme ne fonctionne qu'avec des images au format PNG, JPG ou BMP. Il n'a pas été testé avec des images contenant des transparences.

Auteur
Ce programme a été écrit par Melvin Gueneau.

Licence
Ce programme est distribué sous la licence MIT. Veuillez vous référer au fichier LICENSE pour plus d'informations.
