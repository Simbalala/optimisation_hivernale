# ERO optimisation_hivernale

# Installation

```sh
pip3 install -r requirements.txt
```

# Theorique

Le principe de l'algo est de passer par tout les sommet du graph
au moins une fois.
Tout en realisant le plus cours chemin.

Nous retrouvons un exemple de graph

```sh
python3 theorique/main.py 
```

## Test

```sh
python3 theorique/tests/testsuite.py 
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
    python3 real/main.py -avec 
```

Vous pouver si vous le voulez charger le graph d'un seul arrondissment
ou de toute la ville de Monreal
Ex: anjou

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

