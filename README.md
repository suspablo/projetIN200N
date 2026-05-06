# projetIN200N
Projet 2048 – L1 MIASHS TD1

## Groupe
- Serhane Amine
- Beregoyev Amkhad
- Benabdelkader Jassem
- Hoang Hélène

🔗 https://github.com/suspablo/projetIN200N2048.git

## Description
Ce projet consiste à créer le jeu 2048 en Python.
La version console est terminée et une interface graphique
avec Tkinter a été ajoutée. Le jeu se joue désormais
avec les touches fléchées dans une fenêtre graphique colorée.

## Fonctionnalités terminées

### Version console
- Grille 4x4 initialisée avec des tuiles aléatoires (2 ou 4)
- Déplacements dans les 4 directions (haut, bas, gauche, droite)
- Fusion des tuiles identiques
- Détection de la victoire (tuile 2048 atteinte)
- Détection de la défaite (aucun mouvement possible)
- Calcul et affichage du score

### Interface graphique (Tkinter)
- Fenêtre de jeu avec grille 4x4 colorée
- Couleurs différentes pour chaque valeur de tuile
- Déplacements via les touches fléchées du clavier
- Affichage du score en temps réel
- Popup de victoire et de game over

## Utilisation

### Lancer le jeu
```bash
python main.py
```

### Lancer la démo victoire
```bash
python simulation-fin.py
```

## Fichiers
- `grille.py` : création et affichage de la grille
- `Mouvement.py` : déplacements et fusions
- `conditionreussite.py` : victoire et défaite
- `interface.py` : interface graphique Tkinter
- `simulation-fin.py` : démonstration visuelle d'une grille gagnée
- `main.py` : point d'entrée du jeu

## Répartition
- Amine : GitHub, main.py, demo.py, README
- Hélène : grille.py, interface.py
- Amkhad : Mouvement.py
- Jassem : conditionreussite.py, score

## Sources
- https://en.wikipedia.org/wiki/2048_(video_game)
- https://play2048.co
- https://youtu.be/b4XP2IcI-Bg?si=jk0yCSx2jvBjHlwQ