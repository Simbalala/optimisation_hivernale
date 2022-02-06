# ERO optimisation_hivernale

# Installation

A copier coller afin d'installer les modules nécessaires

```sh
pip3 install -r requirements.txt
```

# MagicScript 

Pour l'etude de notre cas reel nous avons realiser le chemin 
optimal du drone pour la ville de Monreal et par la suite
nous avons decouper la ville de Monreal suivant ces 19
arrondissements.

Ce script nous montre le chemin à parcourir sur l'ensemble de la ville
arrondissement par arrondissement.

```sh
python3 real/main.py -ave
```

## Testsuite

Pour demarrer la testsuite il faut faire la commande suivante

```sh
python3 theorique/tests/testsuite.py -v
```

# Theorique

Le principe de notre algorithme est de passer par tout les sommets du graphe
au moins une fois.
Tout en realisant le plus court chemin.

Nous retrouvons un exemple de graphe

```sh
python3 theorique/main.py 
```

# Real

Pour l'etude de notre cas reel nous avons realiser le chemin 
optimal du drone pour la ville de Monreal et par la suite
nous avons decouper la ville de Monreal suivant ces 19
arrondissement.

Le script peut s'executer de deux maniere different nous avons l'argument
all qui va charger les graphs et les chemins decouper
par arrondissement.

```sh
python3 real/main.py -ave
```

Vous pouver si vous le voulez charger le graphe d'un seul arrondissment
ou de toute la ville de Monreal

Ex: Anjou, Montréal, QC, Canada

```sh
python3 real/main.py -vec 'Montréal, Canada'
python3 real/main.py -vec 'Anjou, Montréal, QC, Canada'
```

# Argument

```sh
optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Start project on 19 sectors of Monreal
  -c CITY, --city CITY  Start project on sector pass in params
  -e, --export          Export path of all graph result is in export folder
  -v, --verbose         See result in console
```