# projetIN200N
Projet 2048 – L1 MIASHS TD1

## Groupe
- Serhane Amine
- Beregoyev Amkhad
- Benabdelkader Jassem
- Hoang Hélène

## Description du projet
Ce projet consiste à créer en Python une version du jeu 2048.
La version console est terminée. L'objectif actuel est de développer une interface graphique.

## Objectif actuel — Interface graphique
- Créer une fenêtre de jeu avec Tkinter
- Afficher la grille avec les tuiles colorées
- Gérer les inputs clavier (flèches directionnelles)
- Afficher le score en temps réel
- Afficher un message de victoire ou de game over

## Fonctionnalités terminées (version console)
- Grille 4x4 initialisée avec des tuiles aléatoires (2 ou 4)
- Déplacements dans les 4 directions (haut, bas, gauche, droite)
- Fusion des tuiles identiques
- Détection de la victoire (tuile 2048 atteinte)
- Détection de la défaite (aucun mouvement possible)
- Calcul et affichage du score

## Structure du code
| Fichier | Rôle |
|---|---|
| `grille.py` | Création, affichage de la grille, ajout de tuiles, score |
| `Mouvement.py` | Déplacements et fusions dans les 4 directions |
| `conditionreussite.py` | Détection victoire et défaite |
| `main.py` | Boucle principale du jeu |

## Répartition des tâches
- **Amine** – Responsable GitHub, `main.py`, score, README, interface graphique
- **Hélène** – `grille.py` : grille, tuiles aléatoires, affichage
- **Amkhad** – `Mouvement.py` : déplacements et fusions
- **Jassem** – `conditionreussite.py` : détection victoire/défaite

## Sources
- https://en.wikipedia.org/wiki/2048_(video_game)
- https://play2048.co




