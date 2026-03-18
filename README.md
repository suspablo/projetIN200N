# projetIN200N
projet 2048 L1 miashs TD1
GROUPE :
 -Serhane Amine 
- Beregoyev Amkhad 
- Benabdelkader Jassem 
- helene 
# Description du projet

Ce projet consiste à implémenter en Python une version console du jeu 2048
## Conditions de réussite

- Le programme permet de jouer une partie complète de 2048 sur une grille 4x4.
- Le joueur peut déplacer les tuiles dans les quatre directions (haut, bas, gauche, droite).
- Les tuiles de même valeur fusionnent correctement et le score est mis à jour.
- Le programme détecte quand une tuile 2048 est atteinte (victoire).

## Conditions d'échec

- La partie est considérée comme terminée lorsque aucun déplacement n'est possible :
  - la grille est pleine,
  - et aucun mouvement ne permet de fusionner deux tuiles adjacentes.
- Dans ce cas, le programme affiche un message de fin de partie et le score final.
Source: - https://en.wikipedia.org/wiki/2048_(video_game)
- https://play2048.co

## Structure du code (temporaire)
Separer le code en plusieur sous code ? 
-On vas d abord faire une fonction pour crée et afficher la grille du jeu #un tableau 4x4 ? 

- Puis une fonction qui sers a afficher le code dans le terminale pour verifier si ca marche 
-Une fonction pour remplir la grille ? selon les regles du jeu on commence avec un deux ou un 4 sur la grille puis vas replacer un deux ou un 4 a chaque mouvement On cherche toutes les cases qui valent 0, on en choisit une au hasard et on y met un 2  ou un 4 !Les chances entre 2 4 a verifier sur le site du createur!!!!!.
- une fonction pour le mouvement : chaque direction aura son propre code 
- une fonction pour verifier les conditions de victoire 
- une fonction qui relance tout si la grille est remplie et que aucune tuile na atteint 2048
6 fonction 
## Repartition des taches 
Pas encore décidé 
