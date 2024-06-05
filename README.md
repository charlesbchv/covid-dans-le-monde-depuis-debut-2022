# Data Science

<p align="center"><a href="https:/laravel.com" target="_blanc"><img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="100"></a></p>
<p align="center"> 
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/charlesbchv/covid-dans-le-monde-depuis-debut-2022">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/charlesbchv/covid-dans-le-monde-depuis-debut-2022">
<img alt="Last commit" src="https://img.shields.io/github/last-commit/charlesbchv/covid-dans-le-monde-depuis-debut-2022">
<img alt="ViewCount" src="https://views.whatilearened.today/views/github/charlesbchv/covid-dans-le-monde-depuis-debut-2022.svg">
<img alt="Bower" src="https://img.shields.io/bower/l/space">
</p>


**Guide d'utilisateur :**
```
Une fois le projet cloné, exécutez `install-library.sh` pour télécharger les librairies nécessaire, afin
de faire fonctionner le code.
Pour executer le fichier, il suffit de se rendre dans le dossier et executer le fichier "traitement_data.py".

Les librairies utilisées sont les suivants : `pip install dash; pip install plotly-express; pip install plotly; pip install pandas.`
```

# COVID-19 dans le monde depuis le début de l'année 2022

Recueil des datas sur le site officiel "**Johns Hopkins Center for Systems Science and Engineering**", qui regroupe les données sur la COVID-19 en temps réel depuis le début de la pandémie. Le lien menant au site des données que j'ai choisi est le suivant : https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases. Vous y trouverez un grand nombre de données sur les cas de COVID-19 dans différents continents, ainsi que des données générales pour tous les pays.

Les données sont organisées en 9 colonnes : *Date, Country, Latitude, Longitude, Soignés, Décès, Active*.



Afin d'obtenir une vision globale de l'évolution de la COVID-19, j'ai choisi de créer un dashbord animé qui permet d'observer l'évolution des cas confirmés depuis le début de l'année 2022 jusqu'à la fin de l'année. Pour lancer le dashbord, il suffit d'appuyer sur le bouton de démarrage.
![play](./ressources/play.png)



Étant donnée que tous les membres de ma famille sont tombées malade récemment, et ce pour la 3ème fois. Je me suis dit pourquoi ne pas analyser le taux de covid dans le monde en 2022, pour voir si covid est aussi présent dans les autres pays. 
![map_2](./ressources/map_2.png)



En France, le taux de personnes atteint par COVID pour l'année 2022 est aussi important, je vous laisse l'aperçu ci-dessus. 
![map_1](./ressources/map_1.png)



D'après les résultats on voit que, comme depuis le début du covid en 2020, les États-Unis sont en tête du classement dans le nombre de cas confirmés & récencés par rapport aux autres pays. Ils ont aussi le plus grand nombre de cas de décès dans le monde. 
![somme](./ressources/somme.png)



Pour cette fin d'année on voit que dans le monde il y a plus de personnes soignées que décédées. 
![fromage](./ressources/fromage.png)



Un aperçu général sur le nombre de décès et le nombre de cas confirmés dans le monde selon les pays.
![confirme_death](./ressources/confirme_death.png)
![analyse](./ressources/analyse.png)


## Organisation du code :

Le code est organisé en 2 parties  :

-  La premiere partie où on déclare les "graphes" qu'on souhaite faire apparaitre sur dashboard
-  Deuxième partie, nous créons le dashboard en lui même dans lequel on organise l'affichage des figures.
  Pour ajouter des éléments au dashboard, il est nécessaire de déclarer de nouvelles figures dans la première partie du code, puis de les inclure dans la déclaration du dashboard.

## Ressources utilisées :

- https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases

© Réalisé par **Charles Batchaev** (E3FI)
